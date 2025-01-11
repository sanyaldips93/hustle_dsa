class CronParser {
  constructor(expression) {
    this.parts = expression.split(' ');
    if (this.parts.length !== 5) {
      throw new Error('Invalid cron expression. Expected 5 fields.');
    }

    this.parsers = [
      new MinuteParser(this.parts[0]),
      new HourParser(this.parts[1]),
      new DayOfMonthParser(this.parts[2]),
      new MonthParser(this.parts[3]),
      new DayOfWeekParser(this.parts[4]),
    ];
  }

  matches(date) {
    return this.parsers.every(parser => parser.matches(date));
  }

  getNext(date) {
    let nextDate = new Date(date.getTime() + 60000); // Start from the next minute
    while (!this.matches(nextDate)) {
      nextDate = new Date(nextDate.getTime() + 60000); // Increment by one minute
    }
    return nextDate;
  }
}

class BaseParser {
  constructor(expression, rangeStart, rangeEnd) {
    this.expression = expression;
    this.rangeStart = rangeStart;
    this.rangeEnd = rangeEnd;

    this.validateExpression();
  }

  validateExpression() {
    if (this.expression === '*') return; // Match everything

    const parsedValues = this.parseExpression();
    if (!parsedValues) {
      throw new Error(`Invalid cron expression: ${this.expression}`);
    }

    for (const value of parsedValues) {
      if (value < this.rangeStart || value > this.rangeEnd) {
        throw new Error(`Value ${value} out of range for ${this.rangeStart}-${this.rangeEnd}`);
      }
    }
  }

  parseExpression() {
    if (this.expression === '*') {
      return null; // Match all
    }
    if (this.expression.includes(',')) {
      return this.expression.split(',').map(Number);
    }
    if (this.expression.includes('-')) {
      const [start, end] = this.expression.split('-').map(Number);
      return Array.from({ length: end - start + 1 }, (_, i) => start + i);
    }
    if (this.expression.includes('/')) {
      const [base, step] = this.expression.split('/').map(Number);
      return Array.from({ length: (this.rangeEnd - base) / step + 1 }, (_, i) => base + i * step);
    }
    const value = Number(this.expression);
    if (isNaN(value)) {
      throw new Error(`Invalid number: ${this.expression}`);
    }
    return [value];
  }
}

class MinuteParser extends BaseParser {
  constructor(expression) {
    super(expression, 0, 59); // Minute range
  }

  matches(date) {
    if (!this.parsedValues) {
      this.parsedValues = this.parseExpression();
    }
    return this.parsedValues === null || this.parsedValues.includes(date.getMinutes());
  }
}

class HourParser extends BaseParser {
  constructor(expression) {
    super(expression, 0, 23); // Hour range
  }

  matches(date) {
    if (!this.parsedValues) {
      this.parsedValues = this.parseExpression();
    }
    return this.parsedValues === null || this.parsedValues.includes(date.getHours());
  }
}

class DayOfMonthParser extends BaseParser {
  constructor(expression) {
    super(expression, 1, 31); // Day range
  }

  matches(date) {
    if (!this.parsedValues) {
      this.parsedValues = this.parseExpression();
    }
    // Handle calendar constraints for months
    const maxDays = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    return (
      this.parsedValues === null ||
      this.parsedValues.some(day => day >= 1 && day <= maxDays)
    );
  }
}

class MonthParser extends BaseParser {
  constructor(expression) {
    super(expression, 1, 12); // Month range
  }

  matches(date) {
    if (!this.parsedValues) {
      this.parsedValues = this.parseExpression();
    }
    return this.parsedValues === null || this.parsedValues.includes(date.getMonth() + 1);
  }
}

class DayOfWeekParser extends BaseParser {
  constructor(expression) {
    super(expression, 0, 6); // Day of week range
  }

  matches(date) {
    if (!this.parsedValues) {
      this.parsedValues = this.parseExpression();
    }
    return this.parsedValues === null || this.parsedValues.includes(date.getDay());
  }
}
