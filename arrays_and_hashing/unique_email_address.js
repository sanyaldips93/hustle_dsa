/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
  const hash = {};
  for(const email of emails) {
      const [name, domain] = email.split('@');
      const nameWithoutDots = name.split('.').join('');
      const nameWithoutDotsAndPlus = nameWithoutDots.split('+')[0];
      if(!hash[domain]) hash[domain] = [nameWithoutDotsAndPlus];
      else if (hash[domain].includes(nameWithoutDotsAndPlus)) continue;
      else hash[domain].push(nameWithoutDotsAndPlus);
  }
  let res = 0; 
  Object.values(hash).forEach(value => res += value.length);
  return res;
};

console.log(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]));