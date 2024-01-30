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
</style>
