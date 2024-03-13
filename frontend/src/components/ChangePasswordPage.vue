<template>
  <div class="modal">
    <div class="modal-content">
      <p>Изменение пароля</p>
      <div class="change-password-modal">
        <div class="input_container">
          <label for="currentPassword">Текущий пароль</label>
          <input v-model="currentPassword" type="password" id="currentPassword" :class="{'input-error': error !== ''}">
        </div>
        <div class="input_container">
          <label for="newPassword">Новый пароль</label>
          <input v-model="newPassword" type="password" id="newPassword">
        </div>
        <div class="input_container">
          <label for="confirmPassword">Повторите новый пароль</label>
          <input v-model="confirmPassword" type="password" id="confirmPassword">
          <div class="error" v-if="error">{{error}}</div>
        </div>
        <div class="button-container">
          <button v-if="showChangeButton" class="button-change_hover" @click="changePassword">Сменить пароль</button>
          <button v-else class="button-change">Сменить пароль</button>
          <button @click="this.$parent.showModal = false" class="button-exit">Отмена</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  data() {
    return {
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',
      showChangeButton: false,
      error: '',
    };
  },
  watch: {
    currentPassword(value) {
      this.showChangeButton = this.newPassword !== '' && this.confirmPassword !== '' && value !== '';
    },
    newPassword(value) {
      this.showChangeButton = this.currentPassword !== '' && this.confirmPassword !== '' && value !== '';
    },
    confirmPassword(value) {
      this.showChangeButton = this.currentPassword !== '' && this.newPassword !== '' && value !== '';
    },
  },
  methods: {
    async changePassword() {
    const data = {
      old_pass: this.currentPassword,
      new_pass: this.newPassword,
      user_id: this.$store.state.registrationData.user_id
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/change_pass_two/', data);
      console.log('Password changed:', response.data);
      this.$parent.showModal = false
    } catch (error) {
      console.error('Error changing password:', error);
      this.error = "Неверный пароль"
    }
  }
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
  z-index: 99;
}

.modal-content {
  width: 20vw;
  height: 40vh;
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
  font-family: TT Norms Medium;
  font-size: 13px;
  font-weight: 500;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  margin: 0;
}
p{
  font-family: TT Norms Medium;
  font-size: 18px;
  font-weight: 500;
  line-height: 21px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  margin: 0;
  margin-bottom: 20px;
}
.button-change{
  background: #4C5D6E33;
  color: #FFFFFF;
}
.button-exit{
  border: 1px solid #4C5D6E33;
  background: #FFFFFF;
  color: #7D838C;
}
input{
  margin-bottom: 0;
}
.button-change_hover{
  background-color:#EFEFFF;
  color: #6266EA;
}
.button-change_hover:hover {
  background-color: #6266EA;
  color: #FFFFFF;
}
.error{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 14px;
  letter-spacing: 0em;
  text-align: left;
  color: #F97F7F;
}
.change-password-modal{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.input-error{
  border: 1px solid #F97F7F; /* устанавливаем стиль границы для случая, когда пароль не верный */
}
.input_container{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.button-exit:hover{
  color: #6266EA;
}

</style>
