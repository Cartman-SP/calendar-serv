<template>
  <div class="modal">
    <div class="modal-content">
      <p>Изменение пароля</p>
      <div class="change-password-modal">
        <div class="input-container">
          <label for="currentPassword">Текущий пароль</label>
          <input type="password" id="currentPassword">
        </div>
        <div class="input-container">
          <label for="newPassword">Новый пароль</label>
          <input type="password" id="newPassword">
        </div>
        <div class="input-container">
          <label for="confirmPassword">Повторите новый пароль</label>
          <input type="password" id="confirmPassword">
        </div>
        <div class="button-container">
          <button @click="changePassword" class="button-change">Сменить пароль</button>
          <button @click="cancelChange" class="button-exit">Отмена</button>
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
  methods: {
    saveName() {
      // Логика сохранения имени
    },
    changePassword() {
      // Логика изменения пароля
      this.showModal = false;
    },
    cancelChange() {
      this.showModal = false;
    },
    // Другие методы, если необходимо
  },
};
</script>

<style scoped>
.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  width: auto;
  height: auto;
  background-color: #FFFFFF;
  padding: 40px;
  border-radius: 8px;
}
.button-container{
  display: flex;
  gap: 10px;
}
label{
  color: #535C69;
  font-family: TT Norms;
  font-size: 13px;
  font-weight: 500;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
}
p{
  font-family: TT Norms;
  font-size: 18px;
  font-weight: 500;
  line-height: 21px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
.button-change{
  background: #4C5D6E33;
}
.button-exit{
  border: 1px solid #4C5D6E33;
  background: #FFFFFF;
  color: #7D838C;
  
}
</style>