<template>
  <div class="modal" v-if="showModal">
    <div class="modal-content">
      <div class="change-password-modal">
        <h3>Изменение пароля</h3>
        <div class="input-container">
          <label for="currentPassword">Текущий пароль</label>
          <input type="password" id="currentPassword" placeholder="Введите текущий пароль">
        </div>
        <div class="input-container">
          <label for="newPassword">Новый пароль</label>
          <input type="password" id="newPassword" placeholder="Введите новый пароль">
        </div>
        <div class="input-container">
          <label for="confirmPassword">Повторите новый пароль</label>
          <input type="password" id="confirmPassword" placeholder="Повторите новый пароль">
        </div>
        <div class="button-container">
          <button @click="changePassword" class="button-change">Сменить пароль</button>
          <button @click="cancelChange" class="button-change">Отмена</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
    };
  },
  methods: {
    saveName() {
      // Логика сохранения имени
    },
    openModal() {
      this.showModal = true;
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

<style>
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
  width: 360px;
  height: 386px;
  background-color: #FFFFFF;
  padding: 20px;
  border-radius: 8px;
}
</style>