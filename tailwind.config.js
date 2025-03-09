/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './scan.html',
    './gallery.html'
  ],
  theme: {
    extend: {
      colors: {
        'purple-900': '#4C1D95',
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
      },
    },
  },
  plugins: [],
}