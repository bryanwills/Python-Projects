/**
 * @typedef {Object} key
 * @property {string} [extra] extra class name
 * @property {string | string[]} value button label(s)
 */

/**
 * @typedef {Object} section
 * @property {string} [extra] extra class name
 * @property {key[]} keys set of keys in the row
 */

/**
 * the list of buttons of the main section
 * @type {section[]}
 */
const mainSection = [
  {
    extra: 'functions',
    keys: [
      { value: 'Esc' },
      { value: 'F1' },
      { value: 'F2' },
      { value: 'F3' },
      { value: 'F4' },
      { value: 'F5' },
      { value: 'F6' },
      { value: 'F7' },
      { value: 'F8' },
      { value: 'F9' },
      { value: 'F10' },
      { value: 'F11' },
      { value: 'F12' }
    ]
  },
  {
    keys: [
      { value: ['`', `~`] },
      { value: ['1', '!'] },
      { value: ['2', '@'] },
      { value: ['3', '#'] },
      { value: ['4', '$'] },
      { value: ['5', '%'] },
      { value: ['6', '^'] },
      { value: ['7', '&'] },
      { value: ['8', '*'] },
      { value: ['9', '('] },
      { value: ['0', ')'] },
      { value: ['-', '_'] },
      { value: ['=', '+'] },
      { value: 'Backspace', extra: 'backspace' }
    ]
  },
  {
    keys: [
      { value: 'Tab', extra: 'tab' },
      { value: 'Q' },
      { value: 'W' },
      { value: 'E' },
      { value: 'R' },
      { value: 'T' },
      { value: 'Y' },
      { value: 'U' },
      { value: 'I' },
      { value: 'O' },
      { value: 'P' },
      { value: ['[', '{'] },
      { value: [']', '}'] },
      { value: ['\\', '|'] }
    ]
  },
  {
    keys: [
      { value: 'Caps Lock', extra: 'capslock' },
      { value: 'A' },
      { value: 'S' },
      { value: 'D' },
      { value: 'F' },
      { value: 'G' },
      { value: 'H' },
      { value: 'J' },
      { value: 'K' },
      { value: 'L' },
      { value: [';', ':'] },
      { value: ["'", '"'] },
      { value: 'Enter', extra: 'enter' }
    ]
  },
  {
    keys: [
      { value: 'Shift', extra: 'shift' },
      { value: 'Z' },
      { value: 'X' },
      { value: 'C' },
      { value: 'V' },
      { value: 'B' },
      { value: 'N' },
      { value: 'M' },
      { value: [',', '<'] },
      { value: ['.', '>'] },
      { value: ['/', '?'] },
      { value: 'Shift', extra: 'shift' }
    ]
  },
  {
    keys: [
      { value: 'Ctrl' },
      { value: 'Fn' },
      { value: '[DEV]', extra: 'dev' },
      { value: 'Alt' },
      { value: 'Space', extra: 'space' },
      { value: 'Alt' },
      { value: 'Ctrl' }
    ]
  }
];

/**
 * the list of buttons of the additional section
 * @type {section[]}
 */
const additionalSection = [
  { extra: 'functions', keys: [{ value: 'PrtScr' }, { value: 'ScrLk' }, { value: 'Pause' }] },
  { extra: 'actions', keys: [{ value: 'Ins' }, { value: 'Home' }, { value: 'PgUp' }] },
  { extra: 'actions', keys: [{ value: 'Del' }, { value: 'End' }, { value: 'PgDn' }] },
  { extra: 'actions', keys: [{ extra: 'empty' }] },
  { extra: 'actions', keys: [{ extra: 'empty' }, { value: '\u2191' }, { extra: 'empty' }] },
  { extra: 'actions', keys: [{ value: '\u2190' }, { value: '\u2193' }, { value: '\u2192' }] }
];

/**
 * parse the array of strings and build a string from the values
 * @param {string[]} values values to be parsed
 * @returns {string}
 */
function toString(values) {
  return values.filter(value => !!value).join(' ');
}

/**
 * create new div element
 * @returns {HTMLDivElement}
 */
function div() {
  return document.createElement('div');
}

/**
 * draw a section
 * @param {section[][]} sections list of sections to be drawn
 */
function draw(sections) {
  // obtaining the container
  const container = document.getElementById('container');

  if (container) {
    // creating keyboard
    const keyboard = div();
    keyboard.className = 'keyboard';
    sections.forEach(rows => {
      // creating section
      const section = div();
      section.className = 'section';
      rows.forEach(data => {
        // creating row
        const row = div();
        row.className = toString(['row', data.extra]);
        if (data.keys instanceof Array) {
          data.keys.forEach(key => {
            // creating button
            const button = div();
            // creating shadow
            const shadow = div();
            const value = key.value instanceof Array ? key.value : [key.value];
            // setting classes
            button.className = toString(['button', key.extra, value.length > 1 ? 'multi' : null]);
            shadow.className = toString(['button', key.extra, 'shadow']);
            // appending the shadow
            button.appendChild(shadow);
            // rendering labels
            value.forEach(item => {
              const label = div();
              label.innerText = item || '';
              button.appendChild(label);
            });
            // appending the button to the row
            row.appendChild(button);
          });
        }
        // appending the row to the section
        section.appendChild(row);
      });
      // appending the section to the keyboard
      keyboard.appendChild(section);
    });

    // adding the overlay
    const overlay = div();
    overlay.className = 'overlay';
    keyboard.appendChild(overlay);

    // appending the keyboard to the container
    container.appendChild(keyboard);
  }
}

/** draw the keyboard */
draw([mainSection, additionalSection]);
