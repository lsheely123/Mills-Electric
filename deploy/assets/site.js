/* Mills Electric Inc — site behaviour
   Brand book v2.0: Signal Red is trim, not a theme.

   The masthead's red hairline is hidden while the navy hero (home) or pagehead
   (inner pages) is still sitting behind the sticky header — a red line on navy
   reads as decoration rather than an edge. Once light content scrolls under the
   header, the line appears and does the job it was specified for.

   The border is always 3px, transparent to red, so nothing reflows. */
(function () {
  'use strict';

  var mast = document.querySelector('.masthead');
  var navy = document.querySelector('.hero, .pagehead');
  if (!mast || !navy) return;

  var queued = false;

  function update() {
    queued = false;
    // the navy band has cleared the header once its bottom edge passes under it
    var cleared = navy.getBoundingClientRect().bottom <= mast.offsetHeight;
    mast.classList.toggle('past-navy', cleared);
  }

  function onChange() {
    if (queued) return;
    queued = true;
    window.requestAnimationFrame(update);
  }

  window.addEventListener('scroll', onChange, { passive: true });
  window.addEventListener('resize', onChange, { passive: true });
  update();
})();
