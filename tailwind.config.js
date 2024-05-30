/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./static/**/*.{html,js}", "./index.html", "./map.html"],
  theme: {
    extend: {
      'colors': {
        'cream': '#FFF9E2',
        'cream-light': '#F9F7EC',
        'cream-dark': '#F0EAD1',  
        'cream-darker': '#D5CFB6',
        'cream-darkest': '#AFA992',
        'cream-background': '#403D30',
        'cream-text': '#F9F7EF',
        'cream-text-light': '#666666',
        'cream-text-dark': '#222222',
        'cream-text-darker': '#111111',
      },

    },
  },
  plugins: [],
}

