<template>
    <div class="main_nav">
        <MenubarComponent :model="items">
          <template #end>
            <div class="flex align-items-center gap-2">
                <InputTextComponent placeholder="Найти" type="text" class="w-8rem sm:w-auto" />
            </div>
        </template>
          <template #item="{ item, props, hasSubmenu, root }">
              <a v-ripple class="flex align-items-center" v-bind="props.action">
                  <span :class="item.icon" />
                  <span class="ml-2">{{ item.label }}</span>
                  <BadgeComponent v-if="item.badge" :class="{ 'ml-auto': !root, 'ml-2': root }" :value="item.badge" />
                  <span v-if="item.shortcut" class="ml-auto border-1 surface-border border-round surface-100 text-xs p-1">{{ item.shortcut }}</span>
                  <i v-if="hasSubmenu" :class="['pi pi-angle-down', { 'pi-angle-down ml-2': root, 'pi-angle-right ml-auto': !root }]"></i>
              </a>
          </template>
      </MenubarComponent>
      </div>
</template>

<script>
export default {
    data() {
        return {
            items: [
                {
                    label: 'Home',
                    icon: 'pi pi-home'
                },
                {
                    label: 'Features',
                    icon: 'pi pi-star'
                },
                {
                    label: 'Projects',
                    icon: 'pi pi-search',
                    items: [
                        {
                            label: 'Core',
                            icon: 'pi pi-bolt',
                            shortcut: '⌘+S'
                        },
                        {
                            label: 'Blocks',
                            icon: 'pi pi-server',
                            shortcut: '⌘+B'
                        },
                        {
                            label: 'UI Kit',
                            icon: 'pi pi-pencil',
                            shortcut: '⌘+U'
                        },
                        {
                            separator: true
                        },
                        {
                            label: 'Templates',
                            icon: 'pi pi-palette',
                            items: [
                                {
                                    label: 'Apollo',
                                    icon: 'pi pi-palette',
                                    badge: 2
                                },
                                {
                                    label: 'Ultima',
                                    icon: 'pi pi-palette',
                                    badge: 3
                                }
                            ]
                        }
                    ]
                },
                {
                    label: 'Contact',
                    icon: 'pi pi-envelope',
                    badge: 3
                }
            ]
        };
    }
};
</script>

<style>
.main_menu {
    text-align: left;
  }
  
  .main_text{
    text-decoration: none;
    color:#535C69;
    text-align: left;
    font-family: "TT Norms";
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: 150%;
  }
  
  .main_nav{
    background-color: #F0F0FD;
    width: 1920px;
    height: 63px;
    border-radius: 5px;
  }
</style>