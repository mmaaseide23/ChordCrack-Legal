(() => {
  'use strict';
  const chords = {
    A: { name: 'A major', frets: [-1, 0, 2, 2, 2, 0], description: 'A major uses C♯. Move that note down one fret to C and you have A minor.' },
    Am: { name: 'A minor', frets: [-1, 0, 2, 2, 1, 0], description: 'A minor uses C. Move that note up one fret to C♯ and you have A major.' },
    E: { name: 'E major', frets: [0, 2, 2, 1, 0, 0], description: 'E major uses G♯. Lift the finger on the G string to hear G in E minor.' },
    Em: { name: 'E minor', frets: [0, 2, 2, 0, 0, 0], description: 'E minor uses the open G string. Fret it once for G♯ and you have E major.' }
  };
  const visual = document.querySelector('.chord-visual');
  let keyboardInput = false;
  document.addEventListener('keydown', () => { keyboardInput = true; });
  document.addEventListener('pointerdown', () => { keyboardInput = false; });
  document.querySelectorAll('input[name="chord"]').forEach(input => {
    input.addEventListener('change', () => {
      const chord = chords[input.value];
      if (!chord || !input.checked) return;
      visual.classList.toggle('keyboard-change', keyboardInput);
      document.querySelector('#chord-name').textContent = chord.name;
      document.querySelector('#chord-symbol').textContent = input.value;
      document.querySelector('#diagram-title').textContent = `${chord.name} chord diagram`;
      document.querySelector('#diagram-desc').textContent = `From low E to high E: ${chord.frets.map(fret => fret < 0 ? 'mute' : fret === 0 ? 'open' : `fret ${fret}`).join(', ')}.`;
      document.querySelector('#chord-description').textContent = chord.description;
      chord.frets.forEach((fret, index) => {
        document.querySelector(`#string-${index}`).textContent = fret < 0 ? '×' : fret === 0 ? '○' : '';
        const dot = document.querySelector(`#dot-${index}`);
        // Keep base SVG geometry stable so only transform and opacity animate.
        const baseY = [87.5, 87.5, 132.5, 132.5, 132.5, 87.5][index];
        dot.style.transform = `translateY(${65 + (Math.max(fret, 1) - .5) * 45 - baseY}px)`;
        dot.style.opacity = fret > 0 ? '1' : '0';
      });
    });
  });
  const menu = document.querySelector('.mobile-menu');
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { menu.open = false; }));
  menu.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu.open) { menu.open = false; menu.querySelector('summary').focus(); }
  });
})();
