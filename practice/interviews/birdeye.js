// We need a timeslot booking system where user can check for the available timeslot, user can book the required timeslot
// post performing the payment.
// Every timeslot has an amount and discount associated.
// Discount will be higher on weekdays and low on weekends.
// Extend this (optional).

// Discount - maybe percentage or value.
// Payment - Net Banking or UPI.










// Payment - type, amount;
// constructor(type, amount);
// function - makePayment(), savePayment();

class Payment {
  constructor(type, amount) {
    this.type = type;
    this.amount = amount;
  }

  makePayment() {}
  savePayment() {}
}


class CardPayment extends Payment{
  constructor(type, amount, cardDetails) {
    super(type, amount);
    this.cardDetails = cardDetails;
  }

  makePayment() {}
  savePayment() {}
}

class UPIPayment extends Payment{
  constructor(type, amount, upiDetails) {
    super(type, amount);
    this.cardDetails = upiDetails;
  }

  makePayment() {}
}


class Discount { // interface
  applyDiscount() {}
}

class PerDiscount { 
  constructor(percentage) {
    this.percentage = percentage;
  }

  applyDiscount() {}
}

class ValueDiscount {
  constructor(val) {
    this.val = val;
  }

  applyDiscount() {}
}

class Person {
  constructor(name, number) {
    this.name = name;
    this.number = number;
  }

  getNumber() {};
  getID() {};
}


class TimeSlot {
  constructor(time, day) {
    this.time = time
    this.day = day
    this.isFree = false;
  }

  checkisFree() {};
  toggleState() {};
}

class TimeSlotManager {
  constructor() {
    // singleton class
  }

  getTimeSlot() {};
  removeTimeSlot() {};
  addTimeSlot() {};
}

class BookingManager {
  constructor() {
    // singleton class
  }

  bookTimeSlot() {};  // orchestrator
}

// class System {
//   TimeSlot timeslot = new TimeSlot();
//   Person per = new Person();
//   TimeSlotManager manager;
//   manager.addTimeSlot(timeSlot);
//   // choose current discount
//   BookingManager bmanager;
//   bmanager.bookTimeSlot(timeslot, per, discount);


// }

