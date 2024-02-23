<template>
    <div class="main">
      <div v-if="filials.length > 0" class="filials">
        <div v-for="filial in filials" :key="filial.id">
          <CardBranch :FilialData="filial"/>
        </div>
        <router-link to="/lk/branch/createbranch" class="add">
          <div class="svg-plus">
            <svg width="1em" height="1em" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg">
              <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z"/>
            </svg>            
          </div>
          <p>Добавить филиал</p>
        </router-link>
      </div>
      <div v-else class="branch">
        <img src="../../static/img/branch.png" alt="" class="img_branch">
        <p class="header">Здесь будет ваш филиал. Будет же?</p>
        <p class="subheader">Осталось только создать виджет, выбрать его оформление и разместить его на сайте или в социальных сетях. После чего ваши клиенты смогут записываться к вам онлайн.</p>
        <a href="#/lk/branch/createbranch" style="text-decoration:none"><button class="branch_btn"> + Добавить филиал</button></a>
      </div>
    </div>
  </template>
  
  <script>
import CardBranch from '../components/CardBranch.vue';

export default {
  components: { CardBranch },
    data() {
      return{
        filials:[
          {
            name: 'хуй',
            adress: 'пизда',
            phone: 'жопа',
            workTime: '123123',
            workDays: '234',
          }
        ]
      };
    }
  }
  </script>
  
  <style scoped>
  .filials{
    display: grid;
    gap: 20px;
    grid-template-columns: repeat(4, 1fr);
  }
  .add {
  text-decoration-line: initial;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  display: flex;
  height: 100%;
  min-height: 250px;
  gap: 10px;
  color: #6266EA;
  border-style: dashed;
  border-width: 2px;
  border-color: #D9D9D9;
  transition: 0.3s ease;
  padding: 20px;
  border-radius: 5px;
}

.add:hover{
  background: #EFEFFF;
}
  .navigation{
    display: flex;
    background-color:#FAFAFA;
  }
  .branch {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 450px;
  }
  
  .img_branch {
    margin-bottom: 10px;
  }
  
  .header {
    color: #535C69;
    font-family: 'TT Norms Medium';
    font-size: 20px;
    font-weight: 500;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: center;
    margin-bottom: 20px;
    margin-top: 20px;
  }
  
  .subheader {
    font-size: 16px;
    line-height: 16px;
    color: #AFB6C1;
    font-family: TT Norms;
    font-weight: 500;
    letter-spacing: 0em;
    text-align: center;
    margin: 0;
    margin-bottom: 20px;
  
  }
  .branch_btn{
    margin: 0 auto;
  }
  </style>