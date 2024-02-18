<template>
    <div class="compo">
        <div class="compo-container">
          <div class="compo-top">
            <img src="../../static/img/case.svg" alt="">
            <p class="compo-text">Твоя краля</p>
          </div>
          <div class="compo-top">
            <img src="../../static/img/geo.svg" alt="">
            <p class="compo-text">г. Павлодар, ул. Членододблина 153/1</p>
          </div>
        </div>
    
        <div class="search">
          <input class="" type="search" name="" id="" placeholder="Найти услугу">
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
</template>

<script>

export default {
  data() {
    return {
      isCircleShown: false, // Added property to track the display of the circle
    };
  },
  methods: {
    toggleSelection() {
    // Toggle between showing the button and the circle
    this.isCircleShown = !this.isCircleShown;
    },
    resetSelection() {
      // Reset to the original state (hide the circle)
      this.isCircleShown = false;
    },
  },  
};
</script>

<style scoped>
.compo{
    width: 30%;
    height: auto;
    background: #FFFFFF;
    border-radius: 25px;
    padding: 10px;
  }
  .compo-container{
    height: 120px;
    border-radius: 5px;
    background: url(../../static/img/salon.png);
  }
  .compo-top{
    display: flex;
    gap: 10px;
  }
  .compo-text{
    color: #FFFFFF;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: 500;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: left;
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
    background: #EBEDFF;
    color: #6266EA;
    font-weight: bold;
    padding: 5px 20px;
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
    background: #6266EA;
    border-radius: 5px;
  }
  p{
    text-align: left;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 17px;
    color:#535C69;
  }
  
</style>