<template>
    <div class="cabinet">
        <div class="navigation">
            <SidebarPage/>
            <div class="lk">
                <NavbarPage/>
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script>
import NavbarPage from './NavbarPage.vue';
import SidebarPage from './SidebarPage.vue';
export default {
    components: { NavbarPage, SidebarPage},
}
</script>

<style>
.navigation{
    display: flex;
}

.cabinet{
    background-color: #FAFAFA;
}

.lk{
    width: 100%;
    height: 80vh;
}
</style>