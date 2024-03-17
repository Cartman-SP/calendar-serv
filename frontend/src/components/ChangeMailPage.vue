<template>
  <div class="modal">
    <div class="modal-content">
      <p>Изменение Email</p>
      <div class="change-password-modal">
        <div class="input_container">
          <label for="currentMail">Новый Email</label>
          <input v-model="currentMail" type="email" id="currentMail">
        </div>
        <div class="input_container">
          <label for="newMail">Повторно введите Email</label>
          <input v-model="newMail" type="email" id="newMail">
        </div>
        <div class="input_container">
          <label for="confirmMail">Текущий пароль</label>
          <input v-model="confirmMail" type="password" id="confirmMail">
        </div>
        <div class="button-container">
          <button v-if="showChangeButton" @click="change_email()" class="button-change_hover">Сменить Email</button>
          <button v-else class="button-change">Сменить Email</button>
          <button @click="cancelChange" class="button-exit">Отмена</button>
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
      currentMail: '',
      newMail: '',
      confirmMail: '',
      showChangeButton: false
    };
  },
  watch: {
    currentMail(value) {
      this.showChangeButton = this.newMail !== '' && this.confirmMail !== '' && value !== '';
    },
    newMail(value) {
      this.showChangeButton = this.currentMail !== '' && this.confirmMail !== '' && value !== '';
    },
    confirmMail(value) {
      this.showChangeButton = this.currentMail !== '' && this.newMail !== '' && value !== '';
    },
  },
  methods:{
    change_email(){
      axios.post('http://127.0.0.1:8000/api/change_mail/',{
        old_mail: this.currentMail,
        new_mail: this.newMail, 
        password: this.confirmMail, 
        user_id: this.$store.state.registrationData.user_id})  
        .then(function (response) {
          console.log(response);
        })

    }
  }
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
}
.button-exit{
  border: 1px solid #4C5D6E33;
  background: #FFFFFF;
  color: #7D838C;
}
input{
  margin-bottom: 20px;
}
.button-change_hover{
  background-color:#EFEFFF;
  color: #6266EA;
}
.button-change_hover:hover {
  background-color: #6266EA;
  color: #FFFFFF;
}
.button-exit:hover{
  color: #6266EA;
}
</style>