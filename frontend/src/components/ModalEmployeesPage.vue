<template>
  <div>
    <div class="overlay"></div>
    <div class="modal-container">
      
      <div class="image-container">
        <img src="../../static/img/sweety.png" alt="" class="sweety">
        <img src="../../static/img/woman_empl.png " alt="" class="woman_service">
      </div>

      <div class="text-container">
        <p class="confirm-head">Супер!<br>Первый сотрудник добавлен</p>
        <p class="confirm-sub">Вероятнее всего у вас есть еще сотрудники, которых мы рекомендуем добавить сейчас.</p>
        <div class="confirms">
          <div class="confirm-service">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#6266EA"/>
            </svg>
            <p class="add-head">Добавить услугу</p>              
          </div>
          <div class="confirm-service">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#6266EA"/>
            </svg>
            <p class="add-head">Добавить сотрудника</p>              
          </div>
          <div class="confirm-service">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#D2D8DE"/>
            </svg>
            <p class="add-sub">Добавить филиал</p>              
          </div>
        </div>
        <div class="btn-wrapper">
          <button class="add-btn" @click="this.$router.push('/dashboard/personal')">Добавить еще сотрудника</button>
          <button class="add-branch" @click="this.$router.push('/dashboard/branch/createbranch')">Добавить филиал</button>
        </div>
      </div>
    </div>
  </div>
  </template>
  
<script>
  export default { 
    data() {
      return {
      };
    },
  };
  </script>
  
  
<style scoped>
.overlay {
  z-index: 98;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6); /* Задний фон с прозрачностью 60% */
}
  .modal-container {
    z-index: 99;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      align-items: center;
      width: 932px;
      height: 560px;
      background-color: #FAFAFA;
      border-radius: 25px;
      box-shadow: 0px 0px 15px 0px rgba(0, 0, 0, 0.10);
    }
    
    .image-container,
    .text-container {
      width: 50%;
      box-sizing: border-box;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    
    .confirm-head {
      color: #535C69;
      font-family: TT Norms Medium;
      font-size: 32px;
      font-style: normal;
      line-height: 120%;
      text-align: left;
    }
    .confirm-sub{
      font-family: TT Norms light;
      font-size: 18px;
      font-weight: 300;
      line-height: 23px;
      letter-spacing: 0em;
      text-align: left;
      color: #535C69;
    }
    p{
      margin: 0;
    }
    .confirms{
      display: flex;
      flex-direction: column;
      gap: 15px;
      margin: 30px 0;
    }
    .confirm-service{
      display: flex;
      gap: 5px;
    }
    .add-head{
      font-family: TT Norms;
      font-size: 14px;
      line-height: 18px;
      letter-spacing: 0em;
      text-align: left;
      color: #535C69;
    }
    .add-sub{
      font-family: TT Norms;
      font-size: 14px;
      font-weight: 500;
      line-height: 18px;
      letter-spacing: 0em;
      text-align: left;
      color: #D2D8DE;
    }
    .btn-wrapper{
      display: flex;
      gap: 20px;
    }
    .add-btn{
      border: 1px solid #DDE1E5;
      background: #FFFFFF;
      color: #AFB6C1;
    }
    .woman_service{
      max-width: 325px;
      max-height: 408px;
      z-index: 1;
    }
    .image-container{
      align-items: center;
    }
    .sweety{
      position: absolute;
      top: 10px;
    }
    .text-container{
      width: 60%;
    }
    .add-branch{
      background: #EFEFFF;
      color: #6266EA;
    }
    .add-branch:hover{
      background: #464AD9;
      color: #FFFFFF;
    }
    .add-btn:hover{
      color: #6266EA;
    }
    @media (max-width: 991px){
      .image-container{
        display: none;
      }
      .modal-container{
        max-width: 690px;
        height: auto;
        padding: 60px;
      }
      .text-container {
        width: 100%;
        padding: 0;
      }
    }
    @media (max-width: 768px){
      .text-container {
        width: 100%;
      }
      .confirm-head {
        color: #535C69;
        font-size: 20px;
        line-height: 20px;
        text-align: center;
      }
      .confirm-sub{
        color: #535C69;
        font-size: 14px;
        line-height: 20px;
        text-align: center;
      }

      .modal-container{
        max-width: 390px;
        height: auto;
      }
    }
    @media (max-width: 576px){
      .btn-wrapper{
        align-items: center;
        flex-direction: column;
        gap: 20px;
      }
      .add-btn{
        width: 100%;
      }
      .add-branch{
        width: 100%;
      }
    }
</style>