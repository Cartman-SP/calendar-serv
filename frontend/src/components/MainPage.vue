<template>
  <div class="main">
    <router-view></router-view>
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
    return {
    };
  },
};
</script>

<style scoped>

.navigation{
  display: flex;
  background-color: white;
}
</style>