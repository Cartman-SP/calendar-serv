<template>
  <div>
    
    <router-view/>
    <nprogress-container></nprogress-container>

  </div>
</template>

<script>
</script>

<style>
button {
  color: var(--ffffff, #FFF);
  background:#6266EA;
  border: none;
  cursor: pointer;
  display: flex;
  height: 36px;
  padding: 10px 14px;
  justify-content: center;
  align-items: center;
  gap: 5px;
  border-radius: 3px;
  transition: all .2s ease;
}
input[type="number"] {
    -moz-appearance: textfield;
  }

  /* Для Webkit (Chrome, Safari) */
  input::-webkit-inner-spin-button,
  input::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }


*,
html * /* override x.xhtml.ru style */ 
{
  scrollbar-width: thin;
  scrollbar-color: #E5E8EB transparent;
}

*::-webkit-scrollbar,
html *::-webkit-scrollbar {
  height: 12px;
  width: 12px;
}
*::-webkit-scrollbar-track,
html *::-webkit-scrollbar-track {
  background: transparent;
}
*::-webkit-scrollbar-thumb,
html *::-webkit-scrollbar-thumb {
  background-color: #E5E8EB;
  border-radius: 5px;
  border: 3px solid transparent;
}

@font-face {
    font-family: 'TT Norms';
    src: url('../static/fonts/TT\ Norms/TTNorms-Regular.eot'), url('../static/fonts/TT\ Norms/TTNorms-Regular.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'TT Norms Bold';
    src: url('../static/fonts/TT\ Norms/TTNorms-Bold.eot'), url('../static/fonts/TT\ Norms/TTNorms-Bold.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'TT Norms Medium';
    src: url('../static/fonts/TT\ Norms/TTNorms-Medium.eot'), url('../static/fonts/TT\ Norms/TTNorms-Medium.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'TT Norms Light';
    src: url('../static/fonts/TT\ Norms/TTNorms-Light.eot'), url('../static/fonts/TT\ Norms/TTNorms-Light.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
}

body{
  margin: 0;
  padding: 0;
  font-family: 'TT Norms';
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  overflow: hidden;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
/* 
button {
    color: var(--ffffff, #FFF);
    background:#6266EA;
    border: none;
    cursor: pointer;
    display: flex;
    height: 36px;
    padding: 10px 14px;
    justify-content: center;
    align-items: center;
    gap: 5px;
    border-radius: 3px;
    outline: none;
  } */

input:focus {
  outline: none;
  border: 1px solid #6266EA;
}

input::placeholder {
  font-family: "TT Norms";
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  color: #D2D8DE;
}

.p-inputswitch-checked{
  background: red;
}


/* Make clicks pass-through */
#nprogress {
  pointer-events: none;
}

#nprogress .bar {
  background: #6266EA;

  position: fixed;
  z-index: 1031;
  top: 0;
  left: 0;

  width: 100%;
  height: 3px;
}

/* Fancy blur effect */
#nprogress .peg {
  display: block;
  position: absolute;
  right: 0px;
  width: 100px;
  height: 100%;
  box-shadow: 0 0 10px #6266EA, 0 0 5px #6266EA;
  opacity: 1.0;

  -webkit-transform: rotate(3deg) translate(0px, -4px);
      -ms-transform: rotate(3deg) translate(0px, -4px);
          transform: rotate(3deg) translate(0px, -4px);
}

/* Remove these to get rid of the spinner */
#nprogress .spinner {
  display: block;
  position: fixed;
  z-index: 1031;
  top: 15px;
  right: 15px;
}

#nprogress .spinner-icon {
  width: 0;
  height: 0;
  box-sizing: border-box;

  border: solid 0px transparent;
  border-top-color: #6266EA;
  border-left-color: #6266EA;
  border-radius: 50%;

  -webkit-animation: nprogress-spinner 400ms linear infinite;
          animation: nprogress-spinner 400ms linear infinite;
}

.nprogress-custom-parent {
  overflow: hidden;
  position: relative;
}

.nprogress-custom-parent #nprogress .spinner,
.nprogress-custom-parent #nprogress .bar {
  position: absolute;
}

@-webkit-keyframes nprogress-spinner {
  0%   { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}
@keyframes nprogress-spinner {
  0%   { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
