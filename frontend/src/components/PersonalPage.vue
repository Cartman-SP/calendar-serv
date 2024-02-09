<template>
    <div class="main">
      <div class="personal">
        <img src="../../static/img/personal.png" alt="" class="img_personal">
        <p class="header">Вот это скорость!</p>
        <p class="subheader">Мы видим, что вы завершили создание услуг. В этом разделе,<br>предлагаем добавить ваших сотрудников и назначить им ранее созданные<br>услуги. Если, у вас нет сотрудников, вы можете пропустить этот шаг<br>и перейти к созданию своего филиала/компании.</p>
        <div class="pernosal_btns">
          <a href="#/lk" style="text-decoration:none"><button class="personal_btn skip-btn"> Пропустить</button></a>
          <a href="#/lk/personal/employees" style="text-decoration:none"><button class="personal_btn"> + Добавить сотрудника</button></a>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return{
  
      };
    }
  }
  </script>
  
  <style scoped>
  .pernosal_btns{
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 10px;
  }

  .skip-btn {
    color: #535C69;
    background: #FFFFFF;
    border-radius: 3px;
    border: 1px solid #DDE1E5
  }
  .navigation{
    display: flex;
    background-color:#FAFAFA;
  }
  .personal {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 560px;
  }
  
  .img_personal {
    margin-bottom: 10px;
  }
  
  .header {
    color: #535C69;
    font-family: "TT Norms";
    font-size: 20px;
    font-weight: 500;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: center;
    margin-bottom: 10px;
  }
  
  .subheader {
    font-size: 16px;
    line-height: 16px;
    color: #AFB6C1;
    font-family: TT Norms;
    font-weight: 500;
    letter-spacing: 0em;
    text-align: center;
  
  }
  .personal_btn{
    margin: 0 auto;
  }
  </style>