<template>
  <div style="display: flex; overflow-y: scroll; height: 86vh;">
    <div class="main">
      <div class="transition">
        <router-link to="/dashboard/widgets" class="employesss-link">Виджеты</router-link>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>
        <p class="creation_text">Создание виджета</p>

      </div>
      <div class="card">
        <div>
          <div class="navigation">
            <div class="settings">
                <div class="forms">
                  <div class="name-container">
                    <div class="input-content">
                      <label for="widgetName">Название виджета</label>
                      <input type="text" id="widgetName" placeholder="Мой виджет" v-model="widgetName">
                    </div>
        
                    <div class="input-content">
                      <label for="widgetLanguage">Язык виджета</label>
                      <SelectPage
                      :options="['Русский', 'Белорусский']"
                      class="select" @input="option => selectedLanguage = option"
                      :placeholderdata="'Выберите язык'"
                      />
                    </div>
                  </div>
                  <div class="filial_container">
                    <div class="label_container">
                      <label for="widgetbranch">Филиалы</label>
                      <Tip :Tip="'Придумать текст.</span>'"/>
                    </div>
                    <SelectPage
                        :options="filials"
                        class="select" @input="handleSelectInput"
                        :placeholderdata="'Выберите филиалы'"
                        />
                        <div class="chips-block">
                          <div class="chip" v-for="chip in filteredChips" :key="chip.id">
                            <svg @click="deleteChip(chip)" width="8" height="8" viewBox="0 0 6 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M2.29294 3.00003L0.146484 5.14648L0.853591 5.85359L3.00004 3.70714L5.1465 5.85359L5.85361 5.14648L3.70715 3.00003L5.85359 0.853591L5.14648 0.146484L3.00004 2.29292L0.853605 0.146484L0.146499 0.853591L2.29294 3.00003Z" fill="white"/>
                            </svg>
                            <p>{{ chip.name }}</p>
                          </div>
                        </div>
                  </div>
              </div>
              <div class="img_container">
                <div class="text_container">
                  <p class="header">Обложка виджета</p>
                  <p class="descr">Выберите фотографию для обложки из ранее загруженных или добавьте новую</p>
                </div>
                <div class="plus_container">
                  <div class="img_plus" @click="uploadImage">
                    <input type="file" style="display: none;" @change="handleImageUpload">
                    <img src="" alt="">
                  </div>
                </div>
              </div>
              <div class="color_container">
                <div class="color">
                  <p class="header">Цветовой схема</p>
                  <div class="switch_container">
                    <p class="light">Светлая</p>
                    <InputSwitchComponent v-model="switches.theme" @change="themechange" style="margin-top: 5px;"/>
                    <p class="dark">Тёмная</p>
                  </div>
                </div>
                <div class="color">
                  <div class="color-text-container">
                    <p class="header">Основной</p>
                    <Tip :Tip="'Основной цвет виджета'"/>
                  </div>
                  <div class="rgb" @click="toggleSelection(1)">
                    <p class="rgb_color">{{ widget.Main }}</p>
                    <div class="rgb_choise" :style="{ backgroundColor: widget.Main }"></div>
                  </div>
                  <PalitraPage v-if="isCircleShown1" class="show" @close="closeall" @updateColor="color => handleColorUpdate(color, 1)"></PalitraPage>
                </div>
                <div class="color">
                  <div class="color-text-container">
                    <p class="header">Фон виджета</p>
                    <Tip :Tip="'Цвет фона виджета'"/>
                  </div>
                  <div class="rgb" @click="toggleSelection(2)">
                    <p class="rgb_color">{{ widget.Back }}</p>
                    <div class="rgb_choise" :style="{ backgroundColor: widget.Back }"></div>
                  </div>
                  <PalitraPage v-if="isCircleShown2" class="show" @close="closeall" @updateColor="color => handleColorUpdate(color, 2)"></PalitraPage>
                </div>
                <div class="color">
                  <div class="color-text-container">
                    <p class="header">Фон плашка</p>
                    <Tip :Tip="'Цвет плашки виджета'"/>
                  </div>
                  <div class="rgb" @click="toggleSelection(3)">
                    <p class="rgb_color">{{ widget.Plashka }}</p>
                    <div class="rgb_choise" :style="{ backgroundColor: widget.Plashka }"></div>
                  </div>
                  <PalitraPage v-if="isCircleShown3" class="show" @close="closeall" @updateColor="color => handleColorUpdate(color, 3)"></PalitraPage>
                </div>
                <div class="color">
                  <div class="color-text-container">
                    <p class="header">Цвет текста</p>
                    <Tip :Tip="'Цвет текста виджета'"/>
                  </div>
                  <div class="rgb" @click="toggleSelection(4)">
                    <p class="rgb_color">{{ widget.Text }}</p>
                    <div class="rgb_choise" :style="{ backgroundColor: widget.Text }"></div>
                  </div>
                  <PalitraPage v-if="isCircleShown4" class="show" @close="closeall" @updateColor="color => handleColorUpdate(color, 4)"></PalitraPage>
                </div>
              </div>
              <div class="window_wrapper">
                <p class="header">Выберите дизайн виджета</p>
                <div class="wrapper">
                  <div class="window_container">
                    <div class="window">
                      <div class="square"></div>
                      <div class="stripe"></div>
                      <div class="stripe"></div>
                      <div class="stripe"></div>
                      <div class="rectangle"></div>
                    </div>
                    <div class="choice" @click="activateChoice" data-type="site">
                      <div class="circle_bottom">
                        <div class="second_circle"></div>
                      </div>
                      <p class="">Виджет в виде сайта</p>
                    </div>
                  </div>
                  <div class="window_container">
                    <div class="window">
                      <div class="stripe"></div>
                      <div class="stripe" style="width:80%"></div>
                      <div class="stripe" style="width:60%"></div>
                      <div class="rectangle"></div>
                    </div>
                    <div class="choice" @click="activateChoice" data-type="embedded">
                      <div class="circle_bottom">
                        <div class="second_circle"></div>
                      </div>
                      <p>Встроенный виджет для вашего сайта</p>
                    </div>
                  </div>
                  <div class="window_container">
                    <div class="window">
                      <div class="lane_container">
                        <div class="lane" style="width:32%"></div>
                        <div class="lane" style="width:62%"></div>
                      </div>
                      <div class="stripe" style="width:80%"></div>
                      <div class="stripe" style="width:60%"></div>
                      <div class="stripe" style="width:40%"></div>
                      <div class="lane_container">
                        <div class="lane" style="width:55%"></div>
                        <div class="circle"></div>
                      </div>
                    </div>
                    <div class="choice" @click="activateChoice" data-type="floating">
                      <div class="circle_bottom">
                        <div class="second_circle"></div>
                      </div>
                      <p>Плавающая кнопка на вашем сайте</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="switch_wrapper">
                <div class="switch">
                  <p class="switch-text">Показывать отзывы?</p>
                  <InputSwitchComponent/>
                </div>
                <div class="switch">
                  <p class="switch-text">Показывать раздел «О нас»?</p>
                  <InputSwitchComponent/>
                </div>
              </div>
              <div class="button-container">
                <button @click="save" class="save-button">Сохранить и выйти</button>
                <button @click="cancel" class="cancel-button">Отмена</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div style="margin-top: 45px;">
      <WidgetConstructor :theme="switches.theme" :MainColor="widget.Main" :WidgetColor="widget.Back" :BakcgroundColor="widget.Plashka" :TextColor="widget.Text" :Filials_ids="this.chips.map(chip => chip.id)"/>  
    </div>
  </div>
</template>
  
<script>
import WidgetConstructor from './WidgetConstructor.vue';
import PalitraPage from './PalitraPage.vue';
import SelectPage from '../components/SelectPage.vue';
import Tip from '../components/TipComponent.vue';
import axios from 'axios';

export default {
  components: { WidgetConstructor , PalitraPage, SelectPage, Tip} ,
  data() {
    return {
      selectedImages: [],
      selectedTab: 'general',
      switches: {
        feedback: false,
        company: false,
        employee: false,
        cancellation: false,
        theme: false,
      },
      selectedChoice: null, 
      isCircleShown1: false,
      isCircleShown2: false, 
      isCircleShown3: false, 
      isCircleShown4: false,

      widget:{
        Main: '#6266EA',
        Back: '#FFFFFF',
        Plashka: '#FAFAFA',
        Text: '#535C69',
      },
      chips: [],
      filials: [],
    };
  },
  computed: {
    filteredChips() {
      // Начинаем с индекса 1 (второй элемент) и возвращаем оставшиеся элементы
      this.chips.forEach(element => {
        console.log(element)
      });
      
      return this.chips.slice(0);
    }
  },
  mounted(){
    this.getfilials()
  },
  methods: {
    getfilials(){
        axios.get(`http://127.0.0.1:8000/api/get_branch/?variable=${this.$store.state.registrationData.user_id}&project=${this.$store.state.activeProjectId}`)
        .then(response => {
            this.filials = response.data;
            this.filials.reverse();
            console.log(this.filials);
            this.branchLoaded = true;
            this.rerenderSidebar();
        })
        .catch(error => {
            console.error('Ошибка при получении данных о пользователе:', error);
        });
    },

    deleteChip(chip){
      let indexToRemove = this.chips.indexOf(chip);
      if (indexToRemove !== -1) {
        this.chips.splice(indexToRemove, 1);
      }
    },

    handleSelectInput(selected) {
      const existingChip = this.chips.find(chip => chip.name === selected.name && chip.id === selected.id);
      if (!existingChip) {
        this.chips.push({ name: selected.name, id: selected.id });
      }
    },

    async handleColorUpdate(color, additionalArgument) {
      switch (additionalArgument) {
        case 1: { this.widget.Main = color; break; }
        case 2: { this.widget.Back = color; break; }
        case 3: { this.widget.Plashka = color; break; }
        case 4: { this.widget.Text = color; break; }
      }
      setTimeout(() => {
        this.closeall();
      }, 0);
    },

    save(){
      const formData = new FormData();
      formData.append('language', this.selectedLanguage);
      //formData.append('link', this.widgetLink);
      formData.append('design', this.widgetDesign);
      formData.append('text', this.widget.Text);
      formData.append('plashka', this.widget.Plashka);
      formData.append('back', this.widget.Back);
      formData.append('main', this.widget.Main);
      formData.append('theme', this.switches.theme);
      formData.append('ogranichenie', this.selectedOgranichenie);
      formData.append('interval', this.selectedInterval);
      formData.append('cancellation', this.switches.cancellation);
      formData.append('employee', this.switches.employee);
      formData.append('company', this.switches.company);
      formData.append('fedback', this.switches.feedback);
      formData.append('branches',  Object.values(this.chips).map(item => item.id).join(','));
      formData.append('name', this.widgetName);
      formData.append('user', this.$store.state.registrationData.user_id);
      formData.append('project', this.$store.state.activeProjectId)      
      this.selectedImages.forEach(image => {formData.append('images[]', image);});
      axios.post('http://127.0.0.1:8000/api/widget_create/', formData)
      .then(response => {
        this.$router.push('/dashboard/widgets/')
        console.log(response);
      })
      .catch(error => {
        // Обработка ошибок
        console.error('Error while posting formData:', error);
      });
    },

    themechange(){
      if (this.switches.theme) {
        this.widget.Main = '#FFC25A'
        this.widget.Back = '#222433'
        this.widget.Plashka = '#1A1B27'
        this.widget.Text = '#F5F5F5'
      }else{
        this.widget.Main = '#6266EA'
        this.widget.Back = '#FFFFFF'
        this.widget.Plashka = '#FAFAFA'
        this.widget.Text = '#535C69'
      }
    },

    uploadImage(event) {
      // Find the associated file input element and trigger a click event
      const fileInput = event.target.querySelector('input[type="file"]');
      if (fileInput) {
        fileInput.click();
      }
    },
    handleImageUpload(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      // Обновляем src изображения
      event.target.closest('.img_plus').querySelector('img').src = e.target.result;
      // Добавляем выбранное изображение в переменную selectedImages
      this.selectedImages.push(file);
    };
    reader.readAsDataURL(file);
  }
},
    toggleSelection(num) {
      switch(num){
        case 1:{ this.isCircleShown1=true;this.isCircleShown2=false;this.isCircleShown3=false;this.isCircleShown4=false;break}
        case 2:{ this.isCircleShown2=true;this.isCircleShown1=false;this.isCircleShown3=false;this.isCircleShown4=false;break}
        case 3:{ this.isCircleShown3=true;this.isCircleShown2=false;this.isCircleShown1=false;this.isCircleShown4=false;break}
        case 4:{ this.isCircleShown4=true;this.isCircleShown2=false;this.isCircleShown3=false;this.isCircleShown1=false;break}
      }
    },
    closeall(){
      this.isCircleShown1=false;
      this.isCircleShown2=false;
      this.isCircleShown3=false;
      this.isCircleShown4=false;
    },
    activateChoice(event) {
      const choice = event.currentTarget;
      const choiceType = choice.getAttribute('data-type');

      this.widgetDesign = choiceType;
      if (this.selectedChoice === choiceType) {
        this.selectedChoice = null;
        choice.querySelector('.second_circle').style.display = 'none';
        choice.querySelector('.circle_bottom').style.borderColor = '#C6CBD2';
      } else {
        this.selectedChoice = choiceType;
        document.querySelectorAll('.choice').forEach(choice => {
          choice.classList.remove('active');
          choice.querySelector('.second_circle').style.display = 'none';
          choice.querySelector('.circle_bottom').style.borderColor = '#C6CBD2';
        });
        choice.classList.add('active');
        choice.querySelector('.second_circle').style.display = 'inline-block';
        choice.querySelector('.circle_bottom').style.borderColor = '#6266EA';
      }
    },
  },
  
};
</script>
  
<style scoped>
.color-text-container{
  display: flex;
  align-items: center;
  justify-content: start;
  gap: 5px;
}
.label_container{
  display: flex;
  gap: 5px;
}
.window_wrapper{
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.img_container{
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.switch_wrapper{
  display: flex;
  gap: 50px;
}
.switch_text{
  font-family: TT Norms Medium;
  font-size: 13px;
  font-weight: 500;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
.switch{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.input-content{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.filial_container{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.forms{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.chip svg:hover path{
  fill: rgb(250, 148, 148);
}
.chips-block{
  width: 100%;
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
  margin-top: 10px;
}

.chip{
  display: flex;
  gap: 5px;
  align-items: center;
  justify-content: start;
  background-color: #6266EA;
  height: 20px;
  padding: 0 15px;
  border-radius: 10px;
  transition: all .2s ease;
}

.chip:hover{
  background-color: #5357c7;
  cursor: pointer;
}

.chip p{
  margin: 0;
  color: white;
  font-family: 'TT Norms';
  font-size: 12px;
  margin-top: -1.5px;
}
.descr{
  font-family: TT Norms Medium;
  font-size: 12px;
  font-weight: 500;
  line-height: 14px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
  width: 100%;
}
.subheader{
  margin-top: 0;
}
.header, .subheader{
  width: fit-content;
}
.name-container{
  display: grid;
  grid-template-columns: 5fr 4fr;
  grid-column-gap: 20px;
  grid-row-gap: 0px; 
}
.apps{
  width: 100%;
}
.app-group{
  display: flex;
  justify-content: start;
  align-items: center;
  gap: 10px;
}
.navigation {
  display: flex;
  background-color:#FAFAFA;
  gap: 40px;
  margin-right: 20px;
}

.settings {
  width: 100%;
  text-align: center;
  height: auto;
  background-color: #FFFFFF;
  padding: 20px;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

label {
  margin-right: 10px;
  margin-bottom: 10px;
  font-family: TT Norms Medium;
  font-size: 13px;
  line-height: 15px;
  letter-spacing: 0em;
  margin: 0;
}

input {
  margin-bottom: 0;
  margin-right: 10px;
}

p{
  text-align: left;
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 17px;
  color:#535C69;
  margin: 0;
}

input::placeholder {
  font-family: "TT Norms Medium";
  font-size: 13px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  color: #D2D8DE;
}

select {
  width: 100%;
  padding: 8px 10px;
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 20px;
  color: #D2D8DE;
  border: none;
  background-color: #F3F5F6;
  margin-bottom: 10px;
  border-radius: 3px;
  height: 36px;
}

select option {
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 20px;
  color: #535C69;
}
.apps-container{
  display: grid;
  grid-template-columns: 5fr 4fr;
  grid-column-gap: 20px;
  grid-row-gap: 0px;
  margin-bottom: 10px;
}
.subheader{
  font-family: TT Norms Medium;
  font-size: 10px;
  font-weight: 500;
  line-height: 12px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
}
.footer{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 20px;
  grid-row-gap: 20px; 
}
.footer-apps{
  display: flex;
  flex-direction: column;
}
.transition {
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin-bottom: 20px;
}

.employesss-link {
  font-family: TT Norms Medium;
  font-size: 20px;
  line-height: 24px;
  text-align: left;
  text-decoration: none;
  color: #AFB6C1;
}

.creation_text {
  color: #535C69;
  font-family: TT Norms Medium;
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0em;
  text-align: left;
  margin: 0;
  width: 100%;
}

.arrow-container {
  display: flex;
  align-items: center;
}

.arrow-icon {
  height: 50%;
}
.plus_container{
  display: flex;
  gap: 10px;
}
.img_plus {
  width: 200px;
  height: 100px;
  border-radius: 5px;
  border: 1px solid #D2D8DE;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: url(../../static/img/plus.svg) center center/cover no-repeat;
  background-size: 10%;
  transition: all .2s ease;
}

.img_plus:hover{
  cursor: pointer;
  background-color: rgb(248, 248, 248);
}

.img_plus img {
  max-width: 100%;
  max-height: 100%;
}
.color_container{
  display: flex;
  gap: 10px;
}
.color{
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 5px;
  position: relative;
}
.rgb{
  height: auto;
  width: 120px;
  border-radius: 3px;
  padding: 5px 10px;
  border: 1px solid #D2D8DE;
  display: flex;
  gap: 10px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
}

.rgb:hover{
  cursor: pointer;
  background-color: rgb(248, 248, 248);
}
.rgb_color{
  margin: 0;
}
.rgb_choise{
  width: 12px;
  height: 12px;
  border: 1px solid #D2D8DE;
  border-radius: 25px;
  margin: 0;
}
.switch_container{
  display: flex;
  align-items: center;
  gap: 10px;
}
.light{
  font-family: TT Norms Medium;
  font-size: 12px;
  font-weight: 500;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  margin: 0;
}
.dark{
  font-family: TT Norms Medium;
  font-size: 12px;
  font-weight: 500;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;    
  margin: 0;
}
.window{
  width: 100%;
  height: 120px;
  border-radius: 2px;
  padding: 15px;
  background: #F6F6F6;
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.stripe {
  background: linear-gradient(90deg, #EBEBEB 0%, #DAE2EE 100%);
  border-radius: 2px;
  width: 100%;
  height: 20px;
}
.square{
  width: 20px;
  height: 45px;
  background: linear-gradient(90deg, #EBEBEB 0%, #DAE2EE 100%);
  border-radius: 2px;
}
.rectangle{
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, #9497FF 0%, #8B8FFF 100%);
  border-radius: 2px;
}
.wrapper{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 20px;
}
.button-container {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  margin-top: 20px;
}
.save-button {
  background-color: #EFEFFF;
  color: #6266EA;
  transition: background-color 0.3s, color 0.3s;
}

.save-button:hover {
  background-color: #464AD9;
  color: #EFEFFF;
}
.cancel-button {
  background-color: #FFFFFF;
  color: #535C69;
  border-radius: 3px;
  border: 1px solid #DDE1E5;
  transition: all 0.2s ease;
}
.cancel-button:hover{
  color: #5357c7;
}
.lane_container{
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}
.lane{
  height: 15px;
  background: linear-gradient(90deg, #EBEBEB 0%, #DAE2EE 100%);
  border-radius: 2px;
}
.circle{
  width: 30px;
  height: 30px;
  background: linear-gradient(90deg, #9497FF 0%, #8B8FFF 100%);
  border-radius: 100px;
}
.card{
  display: flex;
  justify-content: start;
  background: #FAFAFA;
  margin: 10px 0;
}
.tab{
  position: relative;
  border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
  width: 68%;
  display: flex;
  gap: 15px;
  margin-top: 30px;
  padding: 0;
}
.tab-link {
  position: relative;
  font-family: TT Norms Medium;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
  cursor: pointer;
  padding-bottom: 10px;
}
.tab-link:hover {
  color: #6266EA;
}
.tab-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: transparent;
  transition: background-color 0.3s;
}

.tab-link:hover::after {
  background-color: #6266EA;
}
.window_container{
  display: flex;
  flex-direction: column;
}
.active-tab {
  color: #6266EA;
}
.active-tab::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: transparent;
  transition: background-color 0.3s;
  background:#6266EA;
}
.choice{
  display: flex;
  gap: 5px;
  align-items: center;
  cursor: pointer;
  height: 55px;
}
.circle_bottom{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 18px;
  height: 18px;
  border: 1px solid #C6CBD2;
  background: #F3F5F6;
  border-radius: 15px;
  cursor: pointer;
}
.second_circle{
  background: #6266EA;
  width: 10px;
  height: 10px;
  border-radius: 25px;
  display: none;
}
.choice.active .circle_bottom {
  border-color: #6266EA; /* добавили изменение цвета границы для активного choice */
}
@media (max-width: 768px){
  .main{
    padding: 20px;
  }
  #lightmode{
    display: none;
  }
  .window{
    width: 100%;
  }
}
</style>