<template>
    <div class="nav">
        <div class="search">
            <input type="text" placeholder="Найти">
        </div>
        <div class="actions">
            <div class="buttons-menu">
                <div class="showGatesNotifications">
                  <a @click="showGatesNotifications">
                    <svg width="15" height="14" viewBox="0 0 15 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M1.8998 0.299988C1.01615 0.299988 0.299805 1.01633 0.299805 1.89999V12.3C0.299805 13.1836 1.01615 13.9 1.8998 13.9H13.0998C13.9835 13.9 14.6998 13.1836 14.6998 12.3V3.49999C14.6998 2.61633 13.9835 1.89999 13.0998 1.89999H5.8998C5.8998 1.01633 5.18346 0.299988 4.2998 0.299988H1.8998Z" fill="#6266EA"/>
                    </svg>
                  </a>
                  <div  v-if="showGatesNotificationPanel" class="gates-panel">
                    <div class="navbar-arrow"></div>
                    <div>
                      <div class="header">
                        <p>Список проектов</p>
                        <Tip :Width="'350px'" :Tip="'Название компании — это название проекта, \n в проекте собраны: услуги, сотрудники и филиал'"/>
                      </div>
                      <div class="wrapper">
                        <div class="teg" style="justify-content: start;">
                          <div class="teg_svg" :style="{ 'background-color': currentProject.color }">
                            <svg width="16" height="16" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M2 0C0.895431 0 0 0.895431 0 2V15C0 16.1046 0.89543 17 2 17H16C17.1046 17 18 16.1046 18 15V4C18 2.89543 17.1046 2 16 2H7C7 0.895431 6.10457 0 5 0H2Z" fill="white"/>
                            </svg>
                          </div>  
                          <div class="wrapper_name">
                            <p class="wrapper_head">{{ currentProject.name }}</p>
                            <p class="wrapper_subhead">ID {{ currentProject.id }} ({{ currentProject.position }})</p>
                          </div>
                        </div>
                        <input type="search" placeholder="Найти проект">
                        <div class="projects-container">
                          <div class="teg" v-for="p in allPProjects" :key="p">
                            <div style="display: flex; align-items: center; gap: 15px;">
                              <div class="avatar" :style="{ 'background-color': p.color }">
                                <p class="avatar_text">{{ formatText(p.name) }}</p>
                              </div>
                              <div class="wrapper_name">
                                <p class="wrapper_descr">{{ p.name }}</p>
                                <p class="wrapper_subhead">ID {{ p.id }} ({{ p.position }})</p>
                              </div>
                            </div>
                            <div class="actions">
                              <svg id="edit" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0,0,256,256" width="16" height="16"><g fill="#535c69" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(10.66667,10.66667)"><path d="M18,2l-2.41406,2.41406l4,4l2.41406,-2.41406zM14.07617,5.92383l-11.07617,11.07617v4h4l11.07617,-11.07617z"></path></g></g></svg>
                              <svg v-if="p.favourites" id="favourites" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M10.6058 5.56582C10.2353 5.56582 9.90972 5.32907 9.80795 4.98568L9.79389 4.93825C9.79217 4.93245 9.79039 4.92666 9.78853 4.9209L8.58284 1.17581C8.58284 1.17581 8.58284 1.17581 8.58284 1.17581C8.42542 0.686829 7.71354 0.670883 7.53272 1.15228C7.53272 1.15228 7.53272 1.15228 7.53272 1.15228L6.12378 4.90355C6.11727 4.92088 6.11139 4.93841 6.10614 4.95612L6.09737 4.98569C5.9956 5.32907 5.67002 5.56582 5.29955 5.56582H5.26541H1.35465C1.35465 5.56582 1.35465 5.56582 1.35465 5.56582C0.823384 5.56582 0.596976 6.21705 1.02095 6.52567C1.02095 6.52567 1.02095 6.52567 1.02095 6.52567L4.30306 8.91475C4.31602 8.92419 4.32927 8.93326 4.34279 8.94194L4.38432 8.96863C4.68453 9.16158 4.82098 9.51945 4.72186 9.8539L4.7017 9.92191C4.70035 9.92647 4.69895 9.93103 4.69751 9.93557L3.50178 13.7138C3.34596 14.2061 3.93699 14.6015 4.3609 14.2885L7.42053 12.0294C7.42956 12.0227 7.43844 12.0158 7.44717 12.0088L7.46861 11.9916C7.77632 11.7444 8.22329 11.7444 8.531 11.9916L8.55244 12.0088C8.56118 12.0158 8.57006 12.0227 8.57908 12.0294L11.6387 14.2885C12.0626 14.6015 12.6536 14.2061 12.4978 13.7138L11.3021 9.93557C11.3007 9.93103 11.2993 9.92648 11.2979 9.92191L11.2778 9.85391C11.1786 9.51945 11.3151 9.16158 11.6153 8.96863L11.6568 8.94194C11.6703 8.93326 11.6836 8.92419 11.6966 8.91475L14.9787 6.52567C14.9787 6.52567 14.9787 6.52567 14.9787 6.52567C15.4026 6.21705 15.1762 5.56582 14.645 5.56582H10.6399H10.6058Z" fill="#F7D37D"/>
                              </svg>
                              <svg v-else id="favourites" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M10.6058 5.56582C10.2353 5.56582 9.90972 5.32907 9.80795 4.98568L9.79389 4.93825C9.79217 4.93245 9.79039 4.92666 9.78853 4.9209L8.58284 1.17581C8.58284 1.17581 8.58284 1.17581 8.58284 1.17581C8.42542 0.686829 7.71354 0.670883 7.53272 1.15228C7.53272 1.15228 7.53272 1.15228 7.53272 1.15228L6.12378 4.90355C6.11727 4.92088 6.11139 4.93841 6.10614 4.95612L6.09737 4.98569C5.9956 5.32907 5.67002 5.56582 5.29955 5.56582H5.26541H1.35465C1.35465 5.56582 1.35465 5.56582 1.35465 5.56582C0.823384 5.56582 0.596976 6.21705 1.02095 6.52567C1.02095 6.52567 1.02095 6.52567 1.02095 6.52567L4.30306 8.91475C4.31602 8.92419 4.32927 8.93326 4.34279 8.94194L4.38432 8.96863C4.68453 9.16158 4.82098 9.51945 4.72186 9.8539L4.7017 9.92191C4.70035 9.92647 4.69895 9.93103 4.69751 9.93557L3.50178 13.7138C3.34596 14.2061 3.93699 14.6015 4.3609 14.2885L7.42053 12.0294C7.42956 12.0227 7.43844 12.0158 7.44717 12.0088L7.46861 11.9916C7.77632 11.7444 8.22329 11.7444 8.531 11.9916L8.55244 12.0088C8.56118 12.0158 8.57006 12.0227 8.57908 12.0294L11.6387 14.2885C12.0626 14.6015 12.6536 14.2061 12.4978 13.7138L11.3021 9.93557C11.3007 9.93103 11.2993 9.92648 11.2979 9.92191L11.2778 9.85391C11.1786 9.51945 11.3151 9.16158 11.6153 8.96863L11.6568 8.94194C11.6703 8.93326 11.6836 8.92419 11.6966 8.91475L14.9787 6.52567C14.9787 6.52567 14.9787 6.52567 14.9787 6.52567C15.4026 6.21705 15.1762 5.56582 14.645 5.56582H10.6399H10.6058Z" fill="#AFB6C1"/>
                              </svg>
                            </div>
                          </div>
                        </div>
                      </div>
                      <router-link to="/lk/project" style="text-decoration:none; width: fit-content; margin: 15px 0 0 0; height: fit-content;">
                        <div class="bottom">
                          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <g opacity="0.6" clip-path="url(#clip0_4163_7512)">
                            <path d="M13.8366 6.52116C13.6239 6.17809 13.2479 5.97301 12.8309 5.97301H3.54598C3.08573 5.97301 2.66713 6.23245 2.47925 6.63417L0.0234375 11.7832C0.11615 12.1603 0.468308 12.4419 0.887757 12.4419H10.7662C11.1886 12.4419 11.5746 12.2031 11.7632 11.8252L13.8859 7.57069C14.0535 7.23402 14.0349 6.84171 13.8366 6.52116Z" fill="#7D8790" fill-opacity="0.6"/>
                            <path d="M1.97975 5.84217C2.16742 5.44056 2.58612 5.18101 3.04648 5.18101H11.7898V4.06269C11.7898 3.60169 11.4009 3.22657 10.9229 3.22657H5.82476C5.81728 3.22657 5.81215 3.22464 5.81023 3.22326L4.89774 1.94739C4.73613 1.72106 4.46921 1.58594 4.18402 1.58594H0.867096C0.388901 1.58594 0 1.96106 0 2.42206V9.99287L1.97975 5.84217Z" fill="#7D8790" fill-opacity="0.6"/>
                            </g>
                            <defs>
                            <clipPath id="clip0_4163_7512">
                            <rect width="14" height="14" fill="white"/>
                            </clipPath>
                            </defs>
                          </svg>
                          <p class="bottom_text">Всего проектов ({{ allPProjects.length }})</p>
                        </div>
                      </router-link>
                    </div>
                  </div>
                </div>
                
                <div class="showPlusNotifications">
                  <a @click="showPlusNotifications">
                    <svg width="15" height="17" viewBox="0 0 15 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M8.83301 5.16667V0.806667C9.44971 1.03956 10.0099 1.40087 10.4763 1.86667L12.799 4.19067C13.2653 4.65659 13.6269 5.2166 13.8597 5.83333H9.49967C9.32286 5.83333 9.15329 5.7631 9.02827 5.63807C8.90325 5.51305 8.83301 5.34348 8.83301 5.16667ZM14.1663 7.49V13.1667C14.1653 14.0504 13.8138 14.8976 13.1889 15.5225C12.564 16.1474 11.7167 16.4989 10.833 16.5H4.16634C3.28261 16.4989 2.43538 16.1474 1.81049 15.5225C1.1856 14.8976 0.834066 14.0504 0.833008 13.1667V3.83333C0.834066 2.9496 1.1856 2.10237 1.81049 1.47748C2.43538 0.852588 3.28261 0.501059 4.16634 0.5L7.17634 0.5C7.28501 0.5 7.39234 0.508667 7.49967 0.516V5.16667C7.49967 5.6971 7.71039 6.20581 8.08546 6.58088C8.46053 6.95595 8.96924 7.16667 9.49967 7.16667H14.1503C14.1577 7.274 14.1663 7.38133 14.1663 7.49ZM10.1663 11.8333C10.1663 11.6565 10.0961 11.487 9.97108 11.3619C9.84606 11.2369 9.67649 11.1667 9.49967 11.1667H8.16634V9.83333C8.16634 9.65652 8.0961 9.48695 7.97108 9.36193C7.84606 9.23691 7.67649 9.16667 7.49967 9.16667C7.32286 9.16667 7.15329 9.23691 7.02827 9.36193C6.90325 9.48695 6.83301 9.65652 6.83301 9.83333V11.1667H5.49967C5.32286 11.1667 5.15329 11.2369 5.02827 11.3619C4.90325 11.487 4.83301 11.6565 4.83301 11.8333C4.83301 12.0101 4.90325 12.1797 5.02827 12.3047C5.15329 12.4298 5.32286 12.5 5.49967 12.5H6.83301V13.8333C6.83301 14.0101 6.90325 14.1797 7.02827 14.3047C7.15329 14.4298 7.32286 14.5 7.49967 14.5C7.67649 14.5 7.84606 14.4298 7.97108 14.3047C8.0961 14.1797 8.16634 14.0101 8.16634 13.8333V12.5H9.49967C9.67649 12.5 9.84606 12.4298 9.97108 12.3047C10.0961 12.1797 10.1663 12.0101 10.1663 11.8333Z" fill="#6266EA"/>
                    </svg>
                  </a>
                  <div v-if="showPlusNotificationPanel" class="plus-panel">
                    <div class="navbar-arrow"></div>
                    <div class="header">
                      <p>Быстрое создание</p>
                      <Tip :Width="'308px'" :Tip="'Удобно, если заказ был принят по телефону \n и нужно добавить клиента в общую базу'"/>
                    </div>
                    <router-link to="/lk/" style="text-decoration:none" id="drop-menu-href">
                      <div class="create">
                        <svg width="15" height="12" viewBox="0 0 15 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M0.600098 10.8626C0.600098 11.5859 1.34428 12.07 2.00548 11.7768L15.0001 6.01429L2.00699 0.226662C1.34562 -0.0679383 0.600098 0.416118 0.600098 1.14013V3.35045C0.600098 4.39447 1.40314 5.26285 2.44398 5.34435L11.0001 6.01429L2.44944 6.66026C1.40628 6.73907 0.600098 7.60846 0.600098 8.65458V10.8626Z" fill="#6266EA"/>
                        </svg>
                        <p class="subheader">Заявки</p>
                      </div>
                    </router-link>
                    <router-link to="/lk/service/create" style="text-decoration:none" id="drop-menu-href">
                      <div class="create">
                        <svg width="16" height="15" viewBox="0 0 16 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M7.9998 9.10005H15.1998V10.7H7.9998V9.10005Z" fill="#464AD9"/>
                          <path d="M7.9998 12.3H12.7998V13.9H7.9998V12.3Z" fill="#464AD9"/>
                          <path d="M0.799805 9.90005C0.799805 9.45822 1.15798 9.10005 1.5998 9.10005H5.5998C6.04163 9.10005 6.3998 9.45822 6.3998 9.90005V13.9C6.3998 14.3419 6.04163 14.7 5.5998 14.7H1.5998C1.15798 14.7 0.799805 14.3419 0.799805 13.9V9.90005Z" fill="#464AD9"/>
                          <path d="M7.9998 3.50005H12.7998V5.10005H7.9998V3.50005Z" fill="#464AD9"/>
                          <path d="M7.9998 0.300049H15.1998V1.90005H7.9998V0.300049Z" fill="#464AD9"/>
                          <path d="M0.799805 1.10005C0.799805 0.658221 1.15798 0.300049 1.5998 0.300049H5.5998C6.04163 0.300049 6.3998 0.658221 6.3998 1.10005V5.10005C6.3998 5.54188 6.04163 5.90005 5.5998 5.90005H1.5998C1.15798 5.90005 0.799805 5.54188 0.799805 5.10005V1.10005Z" fill="#464AD9"/>
                          </svg>
                        <p class="subheader">Услуги</p>
                      </div>
                    </router-link>
                    <router-link to="/lk/personal/employees" style="text-decoration:none" id="drop-menu-href">
                      <div class="create">
                        <svg width="16" height="13" viewBox="0 0 16 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M12.8 3.69998C12.8 4.80454 11.9046 5.69998 10.8 5.69998C9.69543 5.69998 8.8 4.80454 8.8 3.69998C8.8 2.59541 9.69543 1.69998 10.8 1.69998C11.9046 1.69998 12.8 2.59541 12.8 3.69998Z" fill="#6266EA"/>
                          <path d="M5.6 7.29998H1.6C0.716344 7.29998 0 8.01632 0 8.89997V12.9H10.4V12.1C10.4 9.44901 8.25097 7.29998 5.6 7.29998Z" fill="#6266EA"/>
                          <path d="M16 11.3C16 9.09084 14.2091 7.29998 12 7.29998H8C10.4 7.29998 12.8 9.26465 12.8 12.3233V12.9H16V11.3Z" fill="#6266EA"/>
                          <path d="M7.2 2.89998C7.2 4.44637 5.9464 5.69998 4.4 5.69998C2.8536 5.69998 1.6 4.44637 1.6 2.89998C1.6 1.35358 2.8536 0.0999756 4.4 0.0999756C5.9464 0.0999756 7.2 1.35358 7.2 2.89998Z" fill="#6266EA"/>
                        </svg>
                        <p class="subheader">Сотрудника</p>
                      </div>
                    </router-link>
                    <router-link to="/lk/branch/createbranch" style="text-decoration:none" id="drop-menu-href">
                      <div class="create">
                        <svg width="16" height="15" viewBox="0 0 16 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" clip-rule="evenodd" d="M4 3.70002V3.30002C4 1.97454 5.07452 0.900024 6.4 0.900024H9.6C10.9255 0.900024 12 1.97454 12 3.30002V3.70002H14.4C15.2837 3.70002 16 4.41637 16 5.30002V13.3C16 14.1837 15.2837 14.9 14.4 14.9H1.6C0.716344 14.9 0 14.1837 0 13.3V5.30002C0 4.41637 0.716344 3.70002 1.6 3.70002H4ZM5.6 3.30002C5.6 2.8582 5.95817 2.50002 6.4 2.50002H9.6C10.0418 2.50002 10.4 2.8582 10.4 3.30002V3.70002H5.6V3.30002ZM8 8.50002C8.66274 8.50002 9.2 7.96277 9.2 7.30002C9.2 6.63728 8.66274 6.10002 8 6.10002C7.33726 6.10002 6.8 6.63728 6.8 7.30002C6.8 7.96277 7.33726 8.50002 8 8.50002Z" fill="#6266EA"/>
                        </svg>
                        <p class="subheader">Филиала</p>
                      </div>
                    </router-link>
                  </div>
                </div>
                
                <a href="">
                  <svg width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g clip-path="url(#clip0_4153_4007)">
                    <path d="M6.66225 5.71998C7.20707 5.35912 7.84609 5.16669 8.49958 5.16669C9.15307 5.16669 9.79209 5.35912 10.3369 5.71998L13.6622 2.39464C12.2201 1.17147 10.3906 0.500061 8.49958 0.500061C6.60859 0.500061 4.77903 1.17147 3.33691 2.39464L6.66225 5.71998Z" fill="#6266EA"/>
                    <path d="M14.6056 3.33734L11.2803 6.66267C11.6411 7.2075 11.8336 7.84652 11.8336 8.50001C11.8336 9.1535 11.6411 9.79252 11.2803 10.3373L14.6056 13.6627C15.8288 12.2206 16.5002 10.391 16.5002 8.50001C16.5002 6.60902 15.8288 4.77945 14.6056 3.33734Z" fill="#6266EA"/>
                    <path d="M10.3369 11.28C9.79209 11.6409 9.15307 11.8333 8.49958 11.8333C7.84609 11.8333 7.20707 11.6409 6.66225 11.28L3.33691 14.6054C4.77903 15.8285 6.60859 16.4999 8.49958 16.4999C10.3906 16.4999 12.2201 15.8285 13.6622 14.6054L10.3369 11.28Z" fill="#6266EA"/>
                    <path d="M5.71991 10.3373C5.35906 9.79252 5.16663 9.1535 5.16663 8.50001C5.16663 7.84652 5.35906 7.2075 5.71991 6.66267L2.39458 3.33734C1.17141 4.77945 0.5 6.60902 0.5 8.50001C0.5 10.391 1.17141 12.2206 2.39458 13.6627L5.71991 10.3373Z" fill="#6266EA"/>
                    </g>
                    <defs>
                    <clipPath id="clip0_4153_4007">
                    <rect width="16" height="16" fill="white" transform="translate(0.5 0.5)"/>
                    </clipPath>
                    </defs>
                  </svg>
                </a>
                <div class="showNotifications">
                  <a @click="showNotifications">
                    <svg width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M13.2998 6.9C13.2998 4.20278 12.1067 2.1508 9.98838 1.51001C9.75722 0.922564 9.18914 0.5 8.4998 0.5C7.81423 0.5 7.24859 0.917967 7.01504 1.50041C4.85022 2.1301 3.69981 4.18917 3.69981 6.9C3.69981 8.09303 3.69981 12.5 1.2998 12.5L1.29981 13.3H15.6998V12.5C13.2998 12.5 13.2998 8.1 13.2998 6.9Z" fill="#464AD9"/>
                      <path d="M10.0998 14.9C10.0998 15.7837 9.38346 16.5 8.4998 16.5C7.61615 16.5 6.89981 15.7837 6.89981 14.9H10.0998Z" fill="#464AD9"/>
                    </svg>
                    <div v-if="notifications.length > 0" class="chip"></div>
                  </a>
                  <div v-if="showNotificationPanel" class="notification-panel">
                    <div class="navbar-arrow"></div>
                    <div class="header">
                      <p>Уведомления ({{ notifications.length }})</p>
                      <Tip :Tip="'Уведомления'"/>
                    </div>
                    <div v-if="notifications.length > 0" class="notifications">
                      <div v-for="n in notifications" :key="n" class="create">
                        <p class="subheader">{{ n }}</p>
                      </div>
                    </div>
                    <div v-else>
                      <p class="subheader">У вас нет новых уведомлений</p>
                    </div>
                    <div class="clear-notifications" v-if="notifications.length > 0">
                      <svg width="11" height="12" viewBox="0 0 11 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M8.79961 9.85V4.35H2.19961V9.85C2.19961 10.4575 2.6921 10.95 3.29961 10.95H7.69961C8.30712 10.95 8.79961 10.4575 8.79961 9.85Z" fill="#535C69"/>
                        <path d="M4.09558 1.10807L3.57461 2.15H1.09961V3.25H9.89961V2.15H7.42461L6.90364 1.10806C6.71731 0.735402 6.33642 0.5 5.91977 0.5H5.07945C4.6628 0.5 4.28191 0.735403 4.09558 1.10807Z" fill="#535C69"/>
                      </svg>
                      <p>Очистить уведомления</p>
                    </div>
                  </div>
                </div>
            </div>
            <div class="rate">
                <img src="../../static/img/wallet.svg" alt="231">
                <div class="text">
                    <p>Тариф</p>
                    <h4>{{ rate }}</h4>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Tip from '../components/TipComponent.vue';

export default {
    components: { Tip },
    data() {
        return {
            showNotificationPanel: false,
            showPlusNotificationPanel: false,
            showGatesNotificationPanel: false,
            
            rate: 'Название', //подгружается в название тарифа
            notifications: ['Подтвердите адрес электронной почты', 'popa', 'У вас новая заявка', 'У вас новая заявка', 'popa', 'popa', 'Ваша первая заявка', 'popa', 'popa'], //подгружается в уведомления

            currentProject:{ //подгружается в текущий проект (словарь)
              name: 'Саня пидорас',
              id: '123456',
              position: 'хуево сверстал',
              color: '#F97F7F',
            },

            allPProjects:[ //подгружается в скролл со всеми проектами (массив словарей)
              {
                name: 'Аренда роликов',
                id: '123345',
                position: 'Владелец',
                favourites: false,
                color: '#28CCF0',
              },
              {
                name: 'Гефест центр',
                id: '456723',
                position: 'Администратор',
                favourites: true,
                color: '#F7D37D',
              },
              {
                name: 'Барбер',
                id: '154906',
                position: 'Сотрудник',
                favourites: false,
                color: '#6266EA',
              },
            ],
        };
    },
    methods: {
        showNotifications() {
            this.showNotificationPanel = !this.showNotificationPanel;
            this.showPlusNotificationPanel = false;
            this.showGatesNotificationPanel = false;
        },
        showPlusNotifications() {
            this.showPlusNotificationPanel = !this.showPlusNotificationPanel;
            this.showNotificationPanel = false;
            this.showGatesNotificationPanel = false;
        },
        showGatesNotifications() {
            this.showGatesNotificationPanel = !this.showGatesNotificationPanel;
            this.showNotificationPanel = false;
            this.showPlusNotificationPanel = false;
        },
        formatText(text) {
          return text
            .split(' ')
            .map(word => (word.length > 1 ? word.charAt(0).toUpperCase() : word.toUpperCase()))
            .join('');
        },
    },
};
</script>

<style scoped>
.navbar-arrow {
    position: absolute;
    width: 0;
    height: 0;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-bottom: 10px solid #ffffff;
    top: -9px;
    left: 50%;
    transform: translateX(-50%);
}
.actions{
  display: flex;
  gap: 10px;
}

#edit path{
  fill: #AFB6C1;
}

#edit, #favourites:hover{
  cursor: pointer;
}

#edit:hover path{
  fill: #535C69;
}

#favourites:hover path{
  fill: #F7D37D;
}
.projects-container{
  display: flex;
  flex-direction: column;
  min-height: 150px;
  max-height: 200px;
  overflow-y: scroll;
}
.chip{
  height: 10px;
  width: 10px;
  position: absolute;
  border-radius: 5px;
  background-color: #FFC400;
  right: 0;
  bottom: 0;
}
.clear-notifications{
  display: flex;
  gap: 10px;
  justify-content: start;
  align-items: center;
  font-family: 'TT Norms Medium';
  font-size: 14px;
  margin-top: 10px;
  padding: 10px;
  background-color: white;
  border-radius: 5px;
  transition: all .2s ease;
}

.clear-notifications svg path, .clear-notifications p{
  fill: #535C69;
}

.clear-notifications:hover{
  background-color: rgba(249, 127, 127, 0.2);
  cursor: pointer;
}

.clear-notifications:hover svg path{
  fill: #F97F7F;
}

.clear-notifications:hover p{
  color: #F97F7F;
}
.notifications{
  overflow-y: scroll;
  height: 120px;
}

#drop-menu-href{
  width: 100%;
  margin: 0;
}

.showNotifications{
  position: relative; 
}
.showGatesNotifications{
  position: relative;
}
.showPlusNotifications{
  position: relative;
}

img{
    width: 16px;
}
.nav{
    margin-bottom: 20px;
    height: 4vw;
    width: 100%;
    display: flex;
    background-color: #F3F6F8;
    align-items: center;
    justify-content: space-between;
    padding: 20px;
    border-radius: 10px;
}

.search input{
    background-color: #ffffff;
    color:#D2D8DE;
    margin: 0;
    width: 15vw;
}

.search input:focus{
    outline: none;
    border: 1px solid #6266EA;
}

.actions, .buttons-menu, .rate{
    display: flex;
    align-items: center;
}
.buttons-menu{
  margin-right: 20px;
}

.buttons-menu a{
    position: relative;
    background-color: white;
    width: 40px;
    height: 40px;
    border-radius: 20px;
    margin: 0 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.buttons-menu a:hover svg path{
  fill: #3f43c1;
}

.rate{
    text-align: left;
    background-color: white;
    height: 50px;
    padding: 20px;
    border-radius: 25px;
}

.text{
    margin-left: 20px;
}

.rate p{
    margin: 0;
    color: #D2D8DE;
    font-size: 10px;
}

.rate h4{
    margin: 0;
    color: #52565F;
    font-size: 14px;
}
.notification-panel {
    z-index: 99;
    width: 260px;
    height: fit-content;
    right: -100px;
    top: 50px;
    background-color: #ffffff;
    position: absolute;
    border-radius: 5px;
    padding: 20px;
    text-align: center;
    filter: drop-shadow(0 0 10px rgb(228, 228, 228));
}

.header{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: row;
  font-family: 'TT Norms Medium';
  font-size: 15px;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color:#535C69;
  margin-bottom: 20px;
}
.subheader{
  font-family: 'TT Norms Medium';
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0em;
  text-align: left;
  color:#AFB6C1;
}

.plus-panel {
  width: 260px;
  height: 230px;
  background-color: #ffffff;
  position: absolute;
  z-index: 99;
  right: -100px;
  top: 50px;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
  filter: drop-shadow(0 0 10px rgb(228, 228, 228));
}
.create{
  display: flex;
  gap: 10px;
  padding: 10px;
  width: 100%;
}
.create:hover {
  background-color: #FAFAFA;
  cursor: pointer;
}
.create:hover p {
  color: #535C69;
}

.create svg path{
  fill: #AFB6C1;
}

.create:hover svg path {
  fill: #6266EA;
}
a{
  cursor: pointer;
}
.wrapper_head{
  font-family: 'TT Norms Medium';
  font-size: 13px;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color: #6266EA;
}
.wrapper_subhead{
  font-family: 'TT Norms Medium';
  font-size: 12px;
  line-height: 14px;
  letter-spacing: 0.03em;
  text-align: left;
  color: #AFB6C1;
}
p{
  margin: 0;
}
.teg{
  display: flex;
  justify-content: space-between;
  gap: 10px;
  align-items: center;
  background-color: white;
  padding: 10px;
  border-radius: 5px;
}

.teg:hover{
  background-color: #FAFAFA;
}
.teg_svg{
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #6266EA;
  background: #F97F7F;
  border-radius: 30px;
  height: 36px;
  width: 36px;
}
.wrapper_descr{
  font-family: 'TT Norms Medium';
  font-size: 13px;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
input{
  margin: 0;
}
.avatar{
  height: 32px;
  width: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 30px;
}
.avatar_text{
  margin: -10px;
  font-family: 'TT Norms Medium';
  width: auto;
  height: auto;
  color: #FFFFFF;
  font-size: 14px;
}
.gates-panel {
  filter: drop-shadow(0 0 10px rgb(228, 228, 228));
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 370px;
  height: auto;
  background-color: #ffffff;
  position: absolute;
  right: -155px;
  top: 50px;
  z-index: 99;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
}
.wrapper{
  display: flex;
  flex-direction: column;
  gap: 15px;
  height: 100%;
}
.bottom{
  width: 100%;
  display: flex;
  gap: 5px;
  justify-content: start;
  padding: 0 0 0 10px;
}

.bottom:hover p{
  color: #535C69;
}
.bottom_text{
  font-family: TT Norms Medium;
  font-size: 13px;
  font-weight: 500;
  line-height: 13px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
}
.search input{
  background-image: url(../../static/img/search.svg);
  background-repeat: no-repeat;
  padding-left: 35px;
  background-position: 15px;
}
.wrapper input{
  background-image: url(../../static/img/search.svg);
  background-repeat: no-repeat;
  background-position: calc(100% - 15px) center;
}
</style>