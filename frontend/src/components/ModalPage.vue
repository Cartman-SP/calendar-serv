<template>
    <div>
          <!-- Первый div с картинкой -->
          <div class="image-container">
            <img src="../../static/img/woman.png" alt="" class="woman">
          </div>
    
          <!-- Второй div с текстом и элементами формы -->
          <div class="text-container">
            <p class="days-text">Завершив регистрацию<br>мы подарим вам <span class="days-highlight">365 дней</span><br>бесплатного пользования</p>
            <p class="normal-text">Имя</p>
            <input type="text" placeholder="Введите имя">
            <p class="normal-text">Фотография (необязательно)</p>
            <input type="file" accept="image/*" placeholder="Прикрепите фото">
            <p class="small-text">до 5 МБ, PNG, JPG, JPEG. Для замены - загрузите заново</p>
            <p class="normal-text">Название компании</p>
            <input type="text" v-model="companyName" placeholder="Введите название">
            <p class="small-text">Для ввода доступно — {{ remainingCharacters }}/25</p>
            <button class="continue-button">Продолжить</button>
          </div>
      </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
      companyName: '', // Добавлено свойство данных для названия компании
    };
  },
  computed: {
    remainingCharacters() {
      const maxLength = 25;
      return maxLength - this.companyName.length;
    },
  },
};
</script>

<style>
.modal-container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    justify-content: space-between;
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
  }
  
  .days-text {
    color: #535C69;
    font-family: "TT Norms";
    font-size: 32px;
    font-style: normal;
    font-weight: 500;
    line-height: 120%;
    text-align: left;
  }
  
  .days-highlight {
    color: #6266EA;
    font-family: "TT Norms";
    font-size: 32px;
    font-style: normal;
    font-weight: 500;
    line-height: 120%;
  }
  
  .normal-text {
    color:#535C69;
    font-family: "TT Norms";
    font-size: 13px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    text-align: left;
  }
  
  .small-text {
    color:#D2D8DE;
    font-family: "TT Norms";
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    text-align: left;
  }
  
  .continue-button {
    margin-left: auto;
    margin-top: 20px;
  }
</style>