<template>
  <div>
    <router-view/>
    <MessageAlert :message="'йцвййцйцвйцввцв'" :color="'#0BB6A1'"/>
  </div>
</template>

<script>
import MessageAlert from "./components/MessageAlert.vue";

export default {
  components: { MessageAlert },
}
</script>

<style>
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
    outline: none;
  }

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
</style>
