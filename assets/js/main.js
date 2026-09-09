document.addEventListener('DOMContentLoaded', function () {
  var burger = document.querySelector('.burger');
  var navLinks = document.querySelector('.nav-links');
  if (burger && navLinks) {
    burger.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });
  }

  // Mobile-friendly dropdown toggle (tap to open on small screens)
  document.querySelectorAll('.nav-dropdown > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 1080) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  // Contact form: build a mailto link from the fields and show a thank-you note.
  // (Static site — no backend yet, so this opens the visitor's email client
  // pre-filled with their message rather than submitting silently.)
  var contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = new FormData(contactForm);
      var name = data.get('name') || '';
      var email = data.get('email') || '';
      var phone = data.get('phone') || '';
      var interest = data.get('interest') || '';
      var message = data.get('message') || '';
      var subject = contactForm.dataset.subject || 'Yhteydenotto';
      var bodyLines = [
        (contactForm.dataset.lName || 'Name') + ': ' + name,
        (contactForm.dataset.lEmail || 'Email') + ': ' + email,
        (contactForm.dataset.lPhone || 'Phone') + ': ' + phone,
        (contactForm.dataset.lInterest || 'Interest') + ': ' + interest,
        '', message
      ];
      var mailto = 'mailto:seniorclub@seniorclub.fi'
        + '?subject=' + encodeURIComponent(subject + ' — ' + name)
        + '&body=' + encodeURIComponent(bodyLines.join('\n'));
      window.location.href = mailto;
      var success = document.getElementById('formSuccess');
      if (success) success.classList.add('show');
    });
  }
});
