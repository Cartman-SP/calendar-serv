<template>
    <div class="dropdown-container">
          <div class="dropdown_btn">
            <button @click="toggleDropdown" class="dropdown" :style="{ 'background-color': showDropdown ? '#F3F6F8' : 'transparent' }">
              <img v-if="!showDropdown" src="static/viewapp/img/kebab.svg" alt="Open">
              <img v-if="showDropdown" src="static/viewapp/img/x.svg" alt="Close">
            </button>
          </div>
          <div :class="{'dropdown-menu-show' : showDropdown, 'dropdown-menu-hide' : !showDropdown}">
            <div v-for="button in buttons" :key="button" @click="button.action">
              <div class="dropdown-item">
                <div v-html="button.svg" class="svg-icon">

                </div>
                <div>{{ button.btnname }}</div>
              </div>
              <div v-if="HasDeviders" class="lines"></div>
            </div>
            <div v-if="HasDelete" class="dropdown-item" id="dropdown-delete" @click="callDeleteFunction(); toggleDropdown()">
              <svg style="margin-right: 5px;" width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M3.44318 2.05556C3.44318 1.6797 3.7637 1.375 4.15909 1.375H10.8409C11.2363 1.375 11.5568 1.6797 11.5568 2.05556C11.5568 2.43142 11.2363 2.73611 10.8409 2.73611H4.15909C3.7637 2.73611 3.44318 2.43142 3.44318 2.05556ZM2.96591 5.45833H2.25V4.09722H12.75V5.45833H12.0341V11.1296C12.0341 12.5078 10.8589 13.625 9.4091 13.625H5.59091C4.14116 13.625 2.96591 12.5078 2.96591 11.1296V5.45833ZM10.6023 5.45833H4.39773V11.1296C4.39773 11.7561 4.93194 12.2639 5.59091 12.2639H9.4091C10.0681 12.2639 10.6023 11.7561 10.6023 11.1296V5.45833Z" fill="#AFB6C1"/>
              </svg>
              <div>Удалить</div>
            </div>
          </div>
    </div>  
</template>

<script>
export default {
  props: ['buttons', 'HasDelete', 'HasDeviders'],
    data() {
        return {
        showDropdown: false,
        showModal: false,
        };
    },
    methods: {
        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },

        callDeleteFunction() {
          this.$emit('Deleting')
        }
    }
}
</script>

<style scoped>
img{
  width: 12px;
  height: 12px;
}
.dropdown-container{
    position: relative;
    display: inline-block;
  }
  .dropdown{
    color: #AFB6C1;
    font-size: 15px;
    font-family: 'TT Norms Medium';
    background-color: white;
    width: 2em;
    height: 2em;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 3px;
    transition: all .2s ease;
    border: 1px solid #AFB6C1;
  }
  .dropdown:hover{
    border: 1px solid #535C69;
    cursor: pointer;
  }
  .dropdown-menu-show {
    position: absolute;
    right: 0;
    top: 35px;
    width: 150px;
    height: auto;
    background-color: #FFFFFF;
    border: 1px solid #E4EAEF;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    text-align: left;
    opacity: 1;
    transform: translateY(0px);
    visibility: visible;
    transition: all .2s ease;
  }

  .dropdown-menu-hide {
    position: absolute;
    right: 0;
    top: 35px;
    width: 150px;
    height: auto;
    background-color: #FFFFFF;
    border: 1px solid #E4EAEF;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    text-align: left;
    opacity: 0;
    transform: translateY(5px);
    visibility: hidden;
    transition: all .2s ease;
  }
  
  .dropdown-item{
    display: flex;
    align-items: center;
    justify-content: start;
    padding: 10px;
    font-family: 'TT Norms Medium';
    font-size: 13px;
    font-weight: 500;
    line-height: 13px;
    letter-spacing: 0em;
    color: #AFB6C1;
    transition: all .2s ease;
  }

  .svg-icon >>> svg{
    height: 15px;
    width: 15px;
    margin-right: 5px;
    fill: #AFB6C1;
    transition: all .2s ease;
  }

  .svg-icon >>> svg g{
    fill: #AFB6C1;
    transition: all .2s ease;
  }

  .dropdown-item:hover{
    color: #535C69;
    cursor: pointer;
  }

  .dropdown-item:hover >>> svg{
    fill: #535C69;
  }


  .dropdown-item:hover >>> svg g{
    fill: #535C69;
  }

  #dropdown-delete:hover{
    color: #EF6262;
    cursor: pointer;
  }

  #dropdown-delete:hover svg path{
    fill: #EF6262;
    transition: all .2s ease;
  }

  #dropdown-delete svg path{
    transition: all .2s ease;
  }
  .lines{
    width: 100%;
    height: 1px;
    background-color: #E4EAEF;
  }
  .dropdown_btn{
    display: flex;
    justify-content: right;
  }
  .modal{
    width: 36vw;
    height: auto;
    position: absolute;
    padding: 40px;
    border-radius: 10px;
    gap: 10px;
    left: 500px;
    top: 500px;
    background: white;
  }
  .delete{
    color: #F97F7F;
    background-color: rgba(249, 127, 127, 0.2);
    font-weight: bold;
    transition: all .2s ease;
  }
  .delete:hover{
    background: #F97F7F;
    color: #FFFFFF;
  }
</style>