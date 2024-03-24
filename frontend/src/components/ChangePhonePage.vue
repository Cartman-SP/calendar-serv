<template>
  <div class="modal">
    <div class="modal-content">
      <p>Изменение телефона</p>
      <div class="change-phone-modal">
        <p class="modal_head">Выберете код страны и введите номер телефона.<br> Мы отправим на него код для подтверждения.</p>
        <div class="form-group-phone" style="display: flex;">      
          <div class="card flex justify-content-center">
            <DropdownComponent v-model="selectedCountry" :options="countries" optionLabel="name" placeholder="🇷🇺" class="w-full md:w-14rem">
              <template #value="slotProps">
                <div v-if="slotProps.value" class="flex align-items-center">
                  <div>{{ slotProps.value.name }}</div>
                </div>
                <span v-else>
                  {{ slotProps.placeholder }}
                </span>
              </template>
              <template #option="slotProps">
                <div class="flex align-items-center">
                  <div>{{ slotProps.option.name }}</div>
                </div>
              </template>
            </DropdownComponent>
          </div>
          <InputMaskComponent @input="handleInput" id="basic" v-model="value" :mask="computedMask" :placeholder="computedPlaceholder" />
        </div>
        <div class="button-container">
          <div class="btns">
            <button v-if="showChangeButton" class="button-change_hover" @click="changePhone">Отправить код</button>
            <button v-else class="button-change">Отправить код</button>
            <button @click="this.$parent.showPhone = false" class="button-exit">Отмена</button>
            <div v-if="error">{{error}}</div>
          </div>
          <p class="modal_descr">Политика конфиденциальности</p>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>

export default {
  data() {
    return {
      selectedCountry: null,
      value: '7 ',
      countries: [
        { name: '🇷🇺', code: '+7' },
        { name: '🇧🇾', code: '+375' },
        { name: '🇰🇿', code: '+7' },
        { name: '🇺🇦', code: '+380' },
      ],
      showChangeButton: false,
      error: '',
    };
  },
  computed: {
    computedMask() {
      if (this.selectedCountry) {
        const countryCode = this.selectedCountry.code;
        if (countryCode === '+375' || countryCode === '+380') {
          return `${countryCode} (99) 999-99-99`;
        } else {
          return `${countryCode} (999) 999-99-99`;
        }
      } else {
        return '+7 (999) 999-99-99'; // Default mask
      }
    },
    computedPlaceholder() {
      return this.selectedCountry ? this.selectedCountry.code + ' |' : '+7 |';
    },
  },
  watch: {
    selectedCountry(newCountry) {
      if (newCountry) {
        this.value = newCountry.code + ' ' + this.value.replace(/^\s*\+\d\s*\|\s*/, '');
      }
    },
  },
  methods: {
    handleInput() {
      const countryCode = this.selectedCountry ? this.selectedCountry.code : '';
      this.value = countryCode + ' ' + this.value.replace(/^\s*\+\d\s*\|\s*/, '');
    },
  }
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
  z-index: 99;
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
  line-height: 21px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  margin: 0;
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
  font-family: TT Norms;
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
.button-exit:hover{
  color: #6266EA;
}


</style>
