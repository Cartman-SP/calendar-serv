<template>
    <div class="compo" :id="colortheme">
        <div class="compo-container">
          <div>
            <div class="compo-top">
            <svg width="18" height="18" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M5 4V3.5C5 1.84315 6.34315 0.5 8 0.5H12C13.6569 0.5 15 1.84315 15 3.5V4H18C19.1046 4 20 4.89543 20 6V16C20 17.1046 19.1046 18 18 18H2C0.895431 18 0 17.1046 0 16V6C0 4.89543 0.895431 4 2 4H5ZM7 3.5C7 2.94772 7.44772 2.5 8 2.5H12C12.5523 2.5 13 2.94772 13 3.5V4H7V3.5ZM10 10C10.8284 10 11.5 9.32843 11.5 8.5C11.5 7.67157 10.8284 7 10 7C9.17157 7 8.5 7.67157 8.5 8.5C8.5 9.32843 9.17157 10 10 10Z" fill="white"/>
            </svg>
            <p class="compo-text">Сычевальня</p>
          </div>
          <div class="compo-top">
            <svg width="18" height="18" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M2 7.98124C2 3.52416 5.53247 0 10 0C14.3636 0 18 3.62781 18 7.98124C18 13.3347 10 20 10 20C10 20 2 13.4383 2 7.98124ZM10 11C11.6569 11 13 9.65685 13 8C13 6.34315 11.6569 5 10 5C8.34315 5 7 6.34315 7 8C7 9.65685 8.34315 11 10 11Z" fill="white"/>
            </svg>
            <p class="compo-text">г. Пиводар, ул. Членододблина 1000/3</p>
          </div>
          </div>
          
        </div>
        <div class="compo_main">
          <div class="search">
            <input class="input_search" type="search" name="" id="" placeholder="Найти услугу">
          </div>
      
          <div class="card">
            <div class="compo-wrapper">
              <img src="../../static/img/barber.svg" alt="">
              <p class="">Комплексная мужская<br>стрижка</p>
            </div>
            <div class="compo-wrapper-tariff">
              <div class="tariff">
                <div class="tariff-item">
                  <p>3000 тнг</p>
                </div>
                <div class="dot"></div>
                <div class="tariff-item">
                  <p>1 час</p>
                </div>
              </div>
              <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
              <div v-else class="delete">
                <button @click="resetSelection" class="delete-btn">
                  <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
                </button>
              </div>
            </div>
          </div>
      
          <div class="card">
            <div class="compo-wrapper">
              <img src="../../static/img/barber.svg" alt="">
              <p class="">Комплексная мужская<br>стрижка</p>
            </div>
            <div class="compo-wrapper-tariff">
              <div class="tariff">
                <div class="tariff-item">
                  <p>3000 тнг</p>
                </div>
                <div class="dot"></div>
                <div class="tariff-item">
                  <p>1 час</p>
                </div>
              </div>
              <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
              <div v-else class="delete">
                <button @click="resetSelection" class="delete-btn">
                  <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
                </button>
              </div>
            </div>
          </div>
          <div class="card">
            <div class="compo-wrapper">
              <img src="../../static/img/barber.svg" alt="">
              <p class="">Комплексная мужская<br>стрижка</p>
            </div>
            <div class="compo-wrapper-tariff">
              <div class="tariff">
                <div class="tariff-item">
                  <p>3000 тнг</p>
                </div>
                <div class="dot"></div>
                <div class="tariff-item">
                  <p>1 час</p>
                </div>
              </div>
              <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
              <div v-else class="delete">
                <button @click="resetSelection" class="delete-btn">
                  <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
                </button>
              </div>
            </div>
          </div>
          <div class="card">
            <div class="compo-wrapper">
              <img src="../../static/img/barber.svg" alt="">
              <p class="">Комплексная мужская<br>стрижка</p>
            </div>
            <div class="compo-wrapper-tariff">
              <div class="tariff">
                <div class="tariff-item">
                  <p>3000 тнг</p>
                </div>
                <div class="dot"></div>
                <div class="tariff-item">
                  <p>1 час</p>
                </div>
              </div>
              <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
              <div v-else class="delete">
                <button @click="resetSelection" class="delete-btn">
                  <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
                </button>
              </div>
            </div>
          </div>
          <div class="card">
            <div class="compo-wrapper">
              <img src="../../static/img/barber.svg" alt="">
              <p class="">Комплексная мужская<br>стрижка</p>
            </div>
            <div class="compo-wrapper-tariff">
              <div class="tariff">
                <div class="tariff-item">
                  <p>3000 тнг</p>
                </div>
                <div class="dot"></div>
                <div class="tariff-item">
                  <p>1 час</p>
                </div>
              </div>
              <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
              <div v-else class="delete">
                <button @click="resetSelection" class="delete-btn">
                  <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
                </button>
              </div>
            </div>
          </div>
          <div class="card">
            <div class="compo-wrapper">
              <img src="../../static/img/barber.svg" alt="">
              <p class="">Комплексная мужская<br>стрижка</p>
            </div>
            <div class="compo-wrapper-tariff">
              <div class="tariff">
                <div class="tariff-item">
                  <p>3000 тнг</p>
                </div>
                <div class="dot"></div>
                <div class="tariff-item">
                  <p>1 час</p>
                </div>
              </div>
              <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
              <div v-else class="delete">
                <button @click="resetSelection" class="delete-btn">
                  <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="bottom_container">
          <div class="steps_container">
            <p class="bottom_text">Выбор услуги</p>
            <div class="steps-progress">
              <div class="divider"></div>
              <div class="divider-two"></div>
            </div>
            <p class="steps-text">Шаг 1 из 2</p>
          </div>
          <div class="btn_container">
            <button class="return">
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.3999 6.96667L4.8999 3.5V6.3H13.2999V7.7H4.8999V10.5L1.3999 6.96667Z" fill="#535C69"/>
              </svg>
            </button>
            <button class="next">Далее</button>
          </div>
        </div>
      </div>
</template>

<script>
export default {
  props: ['theme', 'MainColor', 'WidgetColor', 'BakcgroundColor', 'TextColor'],
  watch: {
    theme() {
      this.updateColors();
    },
    MainColor() {
      this.updateColors();
    },
    WidgetColor() {
      this.updateColors();
    },
    BakcgroundColor() {
      this.updateColors();
    },
    TextColor() {
      this.updateColors();
    },
  },
  data() {
    return {
      isCircleShown: false,
      colortheme: 'lightmode',
    };
  },
  methods: {
    toggleSelection() {
      this.isCircleShown = !this.isCircleShown;
    },
    resetSelection() {
      this.isCircleShown = false;
    },
    updateColors() {
      if (this.theme) {
        this.colortheme = 'darkmode';
      } else {
        this.colortheme = 'lightmode';
      }

      if (this.MainColor) {
        this.$el.style.setProperty('--cm', this.MainColor);
        // Изменяем прозрачность и записываем в --cmlight
        const transparentColor = this.changeTransparency(this.MainColor, 0.2); // Здесь 0.2 - это 20% прозрачности, вы можете изменить по вашему усмотрению
        this.$el.style.setProperty('--cmlight', transparentColor);
      }
      if (this.WidgetColor) {
        this.$el.style.setProperty('--cw', this.WidgetColor);
      }
      if (this.BakcgroundColor) {
        this.$el.style.setProperty('--cb', this.BakcgroundColor);
      }
      if (this.TextColor) {
        this.$el.style.setProperty('--ct', this.TextColor);
      }
    },
    changeTransparency(hex, alpha) {
      const isValidHex = /^#([0-9A-Fa-f]{3}){1,2}$/i.test(hex);
      if (!isValidHex) {
        console.error('Invalid HEX color:', hex);
        return hex;
      }

      hex = hex.replace(/^#/, '');
      const bigint = parseInt(hex, 16);

      const r = (bigint >> 16) & 255;
      const g = (bigint >> 8) & 255;
      const b = bigint & 255;

      return `rgba(${r},${g},${b},${alpha})`;
    },
  },
};

</script>

<style scoped>
#lightmode {
  --color-main: var(--cw, white);
  --color-gray: var(--cb, #FAFAFA);
  --color-btnmain: var(--cmlight, #EBEDFF);
  --color-global: var(--cm, #6266EA);
  --color-text: var(--ct, #535C69);
  --color-shadow: rgb(216, 216, 216);
}

#darkmode{
  --color-main: var(--cw, #1A1B27);
  --color-gray: var(--cb, #222433);
  --color-btnmain: var(--cmlight, rgba(255, 194, 90, 0.1));
  --color-global: var(--cm, #FFCF7D);
  --color-text: var(--ct, #F5F5F5);
  --color-shadow: rgb(21, 20, 29);
}

.compo_main{
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 10px;
  height: 470px;
  margin-bottom: -50px;
  overflow: scroll;
  padding-bottom: 50px;
}
.compo{
    width: 20%;
    height: auto;
    background: var(--color-main);
    border-radius: 25px;
    overflow: hidden;
  }
  .compo-container{
    box-shadow: inset 0px -50px 20px rgba(0, 0, 0, 0.698);
    display: flex;
    flex-direction: column;
    justify-content: end;
    gap: 5px;
    height: 120px;
    border-radius: 5px;
    background: url(../../static/img/salon.png) center center/cover no-repeat;
  }
  .compo-top{
    display: flex;
    gap: 10px;
    padding: 5px 10px;
  }
  .compo-text{
    color: #FFFFFF;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: 500;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: left;
    margin: 0;
  }
  .search{
    margin-top:  10px;
  }
  .compo-wrapper{
    display: flex;
    gap: 10px;
  }
  .tariff{
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .compo-wrapper-tariff{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .btn-wrapper{
    border-radius: 100px;
    background: var(--color-btnmain);
    color: var(--color-global);
    font-weight: 500;
    padding: 2px 20px;
  }
  .delete-btn{
    width: 30px;
    height: 30px;
    background-color: rgba(249, 144, 144, 0.1);
    border-radius: 50%;
  }
  .dot {
    display: flex;
    align-items: center;
    height: 2px;
    width: 2px;
    background: var(--color-global);
    border-radius: 5px;
  }
  p{
    text-align: left;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: 500;
    line-height: 17px;
    color:var(--color-text);
  }
  .divider {
    border-bottom: 3px solid var(--color-global); 
    width: 30px;
    border-radius: 100px;
  }
  .divider-two {
    border-bottom: 3px solid #D8DDE3;
    width: 80px;
    border-radius: 100px;
    margin: 10px 0;
  }
  .steps-progress{
    display: flex;
    gap: 5px;
  }
  .steps-text{
    font-size: 8px;
    font-weight: bold;
    line-height: 8px;
    letter-spacing: 0em;
    text-align: left;
    color: var(--color-text);
    margin: 0;
  }
  .return{
    border: 1px solid var(--color-text);
    background: var(--color-main);
    border-radius: 100px;
    width: 30px;
    height: 30px;
    padding: 0;
  }
  .next{
    background-color: var(--color-global);
    border-radius: 100px;
    padding: 10px 20px;
  }
  .btn_container{
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .bottom_container{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;   
    border-radius: 10px;
    background-color: var(--color-main);
    filter: drop-shadow(0 -10px 10px var(--color-shadow));
    position: relative;
    z-index: 10;
  }
  .bottom_text{
    margin: 0;
    font-size: 12px;
    font-weight: bold;
    line-height: 12px;
    letter-spacing: 0em;
    text-align: left;
  }
  .steps_container{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .card{
    background: var(--color-gray);
    border-radius: 10px;
    padding: 5px;
  }
  .input_search{
    margin: 0;
    background-color: var(--color-gray);
  }
</style>