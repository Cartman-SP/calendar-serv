<template>
    <div class="dropdown-container">
          <div class="dropdown_btn">
            <button @blur="showDropdown = false" @click="toggleDropdown" class="dropdown" :style="{ 'background-color': showDropdown ? '#F3F6F8' : 'transparent' }">
                <p>{{ activeChoose }}</p>
                <img src="../../static/img/filter.svg" alt="">
            </button>
          </div>
          <div :class="{'dropdown-menu-show' : showDropdown, 'dropdown-menu-hide' : !showDropdown}">
            <div v-for="button in buttons" :key="button">
              <div class="dropdown-item" @click="choose(button)">
                <div>{{ button }}</div>
              </div>
            </div>
          </div>
    </div>  
</template>

<script>
export default {
    data() {
        return {
            showDropdown: false,
            showModal: false,
            activeChoose: 'Сегодня',

            buttons: ['Сегодня', 'Вчера', '7 дней', '30 дней']
        };
    },
    methods: {
        choose(option){
            this.activeChoose = option
            let formattedOption;
            switch (option) {
                case 'Сегодня':
                    formattedOption = 'today'
                    break;
                case 'Вчера':
                    formattedOption = 'yesterday'
                    break;
                case '7 дней':
                    formattedOption = '7_days'
                    break;
                case '30 дней':
                    formattedOption = '30_days'
                    break;
            
                default:
                    break;
            }
            this.$emit('changed', formattedOption);
        },

        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },
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
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
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
    top: 45px;
    width: 105px;
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
    width: 105px;
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