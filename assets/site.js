/* Mills Electric Inc — site behaviour
   Brand book v3.1: Signal Red is trim, not a theme.

   1. The masthead's red hairline is hidden while the black hero (home) or pagehead
      (inner pages) is still sitting behind the sticky header — red on black is
      4.19:1 and reads as decoration rather than an edge. Once light content scrolls
      under the header, the line appears and does the job it was specified for.
      The border is always 3px, transparent to red, so nothing reflows.

   2. The header floats transparent over the hero/pagehead photo at the very top of
      the page and turns solid black (.is-solid) as soon as the page scrolls. Its
      height is published as --mast-h so the hero and pagehead can pad their copy
      clear of it at every breakpoint.

   3. The header slides away while the reader scrolls down and comes back on any
      scroll up. It never hides near the top of the page or while keyboard focus
      is inside it. Reduced-motion users get the same behaviour without the slide
      (the global reduced-motion rule in site.css removes the transition). */
(function () {
  'use strict';

  var mast = document.querySelector('.masthead');
  if (!mast) return;
  var band = document.querySelector('.hero, .pagehead');

  var root = document.documentElement;
  var queued = false;
  var lastH = 0;
  var lastY = window.scrollY;
  var NUDGE = 6; // px of travel before direction counts, so trackpad jitter doesn't flicker it

  function update() {
    queued = false;
    var h = mast.offsetHeight;
    var y = window.scrollY;

    if (h !== lastH) { root.style.setProperty('--mast-h', h + 'px'); lastH = h; }
    mast.classList.toggle('is-solid', y > 8);

    if (band) {
      // the dark band has cleared the header once its bottom edge passes under it
      mast.classList.toggle('past-dark', band.getBoundingClientRect().bottom <= h);
    }

    if (y <= h || mast.contains(document.activeElement)) {
      mast.classList.remove('mast-hidden');
    } else if (y - lastY > NUDGE) {
      mast.classList.add('mast-hidden');
    } else if (lastY - y > NUDGE) {
      mast.classList.remove('mast-hidden');
    } else {
      return; // too small to count; keep lastY so slow scrolls still add up
    }
    lastY = y;
  }

  function onChange() {
    if (queued) return;
    queued = true;
    window.requestAnimationFrame(update);
  }

  window.addEventListener('scroll', onChange, { passive: true });
  window.addEventListener('resize', onChange, { passive: true });
  mast.addEventListener('focusin', function () { mast.classList.remove('mast-hidden'); });
  update();
})();
