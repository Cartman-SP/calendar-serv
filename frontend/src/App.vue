<template>
  <router-view/>
</template>

<style>

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

body{
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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

  }
</style>
