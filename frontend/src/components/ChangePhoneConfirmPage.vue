<template>
  <div class="modal">
    <div class="modal-content">
      <p>Подтвердите номер телефона</p>
      <div class="change-phone-modal">
        <p class="modal_head">Мы отправили код подтверждения на номер<br>+7 930 071 10 38. Для сохранения номера в<br> настройках профиля введите код</p>
        <div class="input_container">
          <p class="input_head">Код подтверждения</p>
          <input v-model="confirmPhone" type="phone" id="confirmPhone" placeholder="Введите код подтверждения">
          <p class="input_sub">Отправить код повторно (3:44)</p>
        </div>
        <div class="button-container">
          <div class="btns">
            <button class="button-change_hover" @click="changePhone">Подтвердить номер</button>
            <button @click="this.$parent.showModal = false" class="button-exit">Отмена</button>
            <div v-if="error">{{error}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      showChangeButton: false,
      error: '',
    };
  },
};
</script>

<style scoped>
.change-phone-modal{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
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
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.button-container{
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.btns{
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
}
.button-exit{
  border: 1px solid #4C5D6E33;
  background: #FFFFFF;
  color: #7D838C;
}
input{
  margin: 0;
}
.button-change_hover{
  background-color:#EFEFFF;
  color: #6266EA;
}
.button-change_hover:hover {
  background-color: #6266EA;
  color: #FFFFFF;
}
.modal_head{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
.modal_descr{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  color: #7D879099;
}
.input_head{
  font-family: TT Norms Medium;
  font-size: 13px;
  font-weight: 500;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69; 
}
.input_sub{
  font-family: TT Norms Medium;
  font-size: 12px;
  font-weight: 500;
  line-height: 14px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
}
.input_container{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
</style>
