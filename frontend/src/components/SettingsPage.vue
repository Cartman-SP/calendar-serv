<template>
  <div class="main">
    <div class="settings">
    </div>
    <div class="navigation">
      <SidebarPage/>
      <NavbarPage/>
    </div>
  </div>
</template>

<script>
import NavbarPage from './NavbarPage.vue';
import SidebarPage from './SidebarPage.vue';
export default {
  components: { NavbarPage, SidebarPage },
  data() {
    return{

    };
  }
}
</script>

<style scoped>
.navigation{
  display: flex;
  background-color: white;
}
.settings {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 450px;
}

</style>