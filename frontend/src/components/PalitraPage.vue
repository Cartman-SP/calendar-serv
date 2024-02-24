<template>
  <div class="palitra">
    <div class="palitra_container">
      <div class="svg_container">
        <svg width="14" height="14" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M15.5 13C15.2889 13.3561 15.0922 13.6724 14.9095 13.9563C14.578 14.4713 14.2924 14.8796 14.0507 15.2253C13.3313 16.2542 13 16.7279 13 17.8058C13 19.4455 14.3445 20 15.5 20C16.6556 20 18 19.4455 18 17.8058C18 16.7279 17.6687 16.2541 16.9493 15.2253C16.7076 14.8796 16.422 14.4713 16.0905 13.9563C15.9078 13.6724 15.7111 13.3561 15.5 13ZM15.5 14.8791C15.2459 15.2618 15.02 15.5853 14.8315 15.8553C14.6723 16.0833 14.5397 16.2731 14.4395 16.428C14.2565 16.7108 14.1571 16.9049 14.0962 17.0887C14.0376 17.2656 14 17.4786 14 17.8058C14 18.3081 14.1845 18.5515 14.3983 18.7043C14.659 18.8907 15.0592 19 15.5 19C15.9408 19 16.341 18.8907 16.6017 18.7043C16.8155 18.5515 17 18.3081 17 17.8058C17 17.4786 16.9624 17.2656 16.9038 17.0887C16.8429 16.9049 16.7435 16.7108 16.5605 16.428C16.4603 16.2731 16.3277 16.0833 16.1685 15.8553C15.98 15.5853 15.7541 15.2618 15.5 14.8791Z" fill="white"/>
          <path fill-rule="evenodd" clip-rule="evenodd" d="M0 11.6739C6.30924e-05 11.8455 0.0394801 12.0171 0.118251 12.1735C0.168734 12.2738 0.235381 12.3679 0.318191 12.4518L6.46364 18.6776C6.88789 19.1075 7.57575 19.1075 8 18.6776L15.6818 10.8953C16.1061 10.4655 16.1061 9.76863 15.6818 9.33882L6.46364 0L5.69546 0.665295L8 3L0.318191 10.8953C0.23538 10.9792 0.168733 11.0733 0.11825 11.1735C0.0394799 11.33 6.30922e-05 11.5024 0 11.6739ZM1.44866 12.1735L7.17533 17.9751C7.20803 18.0083 7.25561 18.0083 7.28831 17.9751L13.015 12.1735H1.44866ZM14.0021 11.1735H1.4427L8.71245 3.70175L14.9701 10.0413C14.9888 10.0602 15 10.0857 15 10.1171C15 10.1484 14.9888 10.1739 14.9701 10.1928L14.0021 11.1735Z" fill="white"/>
        </svg>  
      </div>
      <p style="width: auto;">Основной цвет</p>
      <div class="circle_container">
        <div class="palitra_circle" @click="this.$parent.closeall">
          <svg width="12" height="12" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M8.58578 10L4.29288 14.2929L5.70709 15.7071L10 11.4142L14.2929 15.7071L15.7071 14.2929L11.4142 10L15.7071 5.70712L14.2929 4.29291L10 8.58579L5.70712 4.29291L4.29291 5.70712L8.58578 10Z" fill="#AFB6C1"/>
          </svg>
        </div>
      </div>
    </div>
    <div class="palette">
      <div class="main_color" style="background:#FEFFFE" @click="selectedColor = '#FEFFFE'; selectColor()"></div>
      <div class="main_color" style="background:#EBEBEB" @click="selectedColor = '#EBEBEB'; selectColor()"></div>
      <div class="main_color" style="background:#D6D6D6" @click="selectedColor = '#D6D6D6'; selectColor()"></div>
      <div class="main_color" style="background:#C2C2C2" @click="selectedColor = '#C2C2C2'; selectColor()"></div>
      <div class="main_color" style="background:#ADADAD" @click="selectedColor = '#ADADAD'; selectColor()"></div>
      <div class="main_color" style="background:#999999" @click="selectedColor = '#999999'; selectColor()"></div>
      <div class="main_color" style="background:#858585" @click="selectedColor = '#858585'; selectColor()"></div>
      <div class="main_color" style="background:#707070" @click="selectedColor = '#707070'; selectColor()"></div>
      <div class="main_color" style="background:#5C5C5C" @click="selectedColor = '#5C5C5C'; selectColor()"></div>
      <div class="main_color" style="background:#474747" @click="selectedColor = '#474747'; selectColor()"></div>
      <div class="main_color" style="background:#333333" @click="selectedColor = '#333333'; selectColor()"></div>
      <div class="main_color" style="background:#000000" @click="selectedColor = '#000000'; selectColor()"></div>
      <div class="main_color" style="background:#00374A" @click="selectedColor = '#00374A'; selectColor()"></div>
      <div class="main_color" style="background:#011D57" @click="selectedColor = '#011D57'; selectColor()"></div>
      <div class="main_color" style="background:#11053B" @click="selectedColor = '#11053B'; selectColor()"></div>
      <div class="main_color" style="background:#2E063D" @click="selectedColor = '#2E063D'; selectColor()"></div>
      <div class="main_color" style="background:#3C071B" @click="selectedColor = '#3C071B'; selectColor()"></div>
      <div class="main_color" style="background:#5C0701" @click="selectedColor = '#5C0701'; selectColor()"></div>
      <div class="main_color" style="background:#5A1C00" @click="selectedColor = '#5A1C00'; selectColor()"></div>
      <div class="main_color" style="background:#583300" @click="selectedColor = '#583300'; selectColor()"></div>
      <div class="main_color" style="background:#563D00" @click="selectedColor = '#563D00'; selectColor()"></div>
      <div class="main_color" style="background:#666100" @click="selectedColor = '#666100'; selectColor()"></div>
      <div class="main_color" style="background:#4F5504" @click="selectedColor = '#4F5504'; selectColor()"></div>
      <div class="main_color" style="background:#263E0F" @click="selectedColor = '#263E0F'; selectColor()"></div>
      <div class="main_color" style="background:#004D65" @click="selectedColor = '#004D65'; selectColor()"></div>
      <div class="main_color" style="background:#012F7B" @click="selectedColor = '#012F7B'; selectColor()"></div>
      <div class="main_color" style="background:#1A0A52" @click="selectedColor = '#1A0A52'; selectColor()"></div>
      <div class="main_color" style="background:#450D59" @click="selectedColor = '#450D59'; selectColor()"></div>
      <div class="main_color" style="background:#551029" @click="selectedColor = '#551029'; selectColor()"></div>
      <div class="main_color" style="background:#831100" @click="selectedColor = '#831100'; selectColor()"></div>
      <div class="main_color" style="background:#7B2900" @click="selectedColor = '#7B2900'; selectColor()"></div>
      <div class="main_color" style="background:#7A4A00" @click="selectedColor = '#7A4A00'; selectColor()"></div>
      <div class="main_color" style="background:#785800" @click="selectedColor = '#785800'; selectColor()"></div>
      <div class="main_color" style="background:#8D8602" @click="selectedColor = '#8D8602'; selectColor()"></div>
      <div class="main_color" style="background:#6F760A" @click="selectedColor = '#6F760A'; selectColor()"></div>
      <div class="main_color" style="background:#38571A" @click="selectedColor = '#38571A'; selectColor()"></div>
      <div class="main_color" style="background:#016E8F" @click="selectedColor = '#016E8F'; selectColor()"></div>
      <div class="main_color" style="background:#0042A9" @click="selectedColor = '#0042A9'; selectColor()"></div>
      <div class="main_color" style="background:#2C0977" @click="selectedColor = '#2C0977'; selectColor()"></div>
      <div class="main_color" style="background:#61187C" @click="selectedColor = '#61187C'; selectColor()"></div>
      <div class="main_color" style="background:#791A3D" @click="selectedColor = '#791A3D'; selectColor()"></div>
      <div class="main_color" style="background:#B51A00" @click="selectedColor = '#B51A00'; selectColor()"></div>
      <div class="main_color" style="background:#AD3E00" @click="selectedColor = '#AD3E00'; selectColor()"></div>
      <div class="main_color" style="background:#A96800" @click="selectedColor = '#A96800'; selectColor()"></div>
      <div class="main_color" style="background:#A67B01" @click="selectedColor = '#A67B01'; selectColor()"></div>
      <div class="main_color" style="background:#C4BC00" @click="selectedColor = '#C4BC00'; selectColor()"></div>
      <div class="main_color" style="background:#9BA50E" @click="selectedColor = '#9BA50E'; selectColor()"></div>
      <div class="main_color" style="background:#4E7A27" @click="selectedColor = '#4E7A27'; selectColor()"></div>
      <div class="main_color" style="background:#008CB4" @click="selectedColor = '#008CB4'; selectColor()"></div>
      <div class="main_color" style="background:#0056D6" @click="selectedColor = '#0056D6'; selectColor()"></div>
      <div class="main_color" style="background:#371A94" @click="selectedColor = '#371A94'; selectColor()"></div>
      <div class="main_color" style="background:#7A219E" @click="selectedColor = '#7A219E'; selectColor()"></div>
      <div class="main_color" style="background:#99244F" @click="selectedColor = '#99244F'; selectColor()"></div>
      <div class="main_color" style="background:#E22400" @click="selectedColor = '#E22400'; selectColor()"></div>
      <div class="main_color" style="background:#DA5100" @click="selectedColor = '#DA5100'; selectColor()"></div>
      <div class="main_color" style="background:#D38301" @click="selectedColor = '#D38301'; selectColor()"></div>
      <div class="main_color" style="background:#D19D01" @click="selectedColor = '#D19D01'; selectColor()"></div>
      <div class="main_color" style="background:#F5EC00" @click="selectedColor = '#F5EC00'; selectColor()"></div>
      <div class="main_color" style="background:#C3D117" @click="selectedColor = '#C3D117'; selectColor()"></div>
      <div class="main_color" style="background:#669D34" @click="selectedColor = '#669D34'; selectColor()"></div>
      <div class="main_color" style="background:#00A1D8" @click="selectedColor = '#00A1D8'; selectColor()"></div>
      <div class="main_color" style="background:#0061FD" @click="selectedColor = '#0061FD'; selectColor()"></div>
      <div class="main_color" style="background:#4D22B2" @click="selectedColor = '#4D22B2'; selectColor()"></div>
      <div class="main_color" style="background:#982ABC" @click="selectedColor = '#982ABC'; selectColor()"></div>
      <div class="main_color" style="background:#B92D5D" @click="selectedColor = '#B92D5D'; selectColor()"></div>
      <div class="main_color" style="background:#FF4015" @click="selectedColor = '#FF4015'; selectColor()"></div>
      <div class="main_color" style="background:#FF6A00" @click="selectedColor = '#FF6A00'; selectColor()"></div>
      <div class="main_color" style="background:#FFAB01" @click="selectedColor = '#FFAB01'; selectColor()"></div>
      <div class="main_color" style="background:#FCC700" @click="selectedColor = '#FCC700'; selectColor()"></div>
      <div class="main_color" style="background:#FEFB41" @click="selectedColor = '#FEFB41'; selectColor()"></div>
      <div class="main_color" style="background:#D9EC37" @click="selectedColor = '#D9EC37'; selectColor()"></div>
      <div class="main_color" style="background:#76BB40" @click="selectedColor = '#76BB40'; selectColor()"></div>
      <div class="main_color" style="background:#01C7FC" @click="selectedColor = '#01C7FC'; selectColor()"></div>
      <div class="main_color" style="background:#3A87FD" @click="selectedColor = '#3A87FD'; selectColor()"></div>
      <div class="main_color" style="background:#5E30EB" @click="selectedColor = '#5E30EB'; selectColor()"></div>
      <div class="main_color" style="background:#BE38F3" @click="selectedColor = '#BE38F3'; selectColor()"></div>
      <div class="main_color" style="background:#E63B7A" @click="selectedColor = '#E63B7A'; selectColor()"></div>
      <div class="main_color" style="background:#FE6250" @click="selectedColor = '#FE6250'; selectColor()"></div>
      <div class="main_color" style="background:#FE8648" @click="selectedColor = '#FE8648'; selectColor()"></div>
      <div class="main_color" style="background:#FEB43F" @click="selectedColor = '#FEB43F'; selectColor()"></div>
      <div class="main_color" style="background:#FECB3E" @click="selectedColor = '#FECB3E'; selectColor()"></div>
      <div class="main_color" style="background:#FFF76B" @click="selectedColor = '#FFF76B'; selectColor()"></div>
      <div class="main_color" style="background:#E4EF65" @click="selectedColor = '#E4EF65'; selectColor()"></div>
      <div class="main_color" style="background:#96D35F" @click="selectedColor = '#96D35F'; selectColor()"></div>
      <div class="main_color" style="background:#52D6FC" @click="selectedColor = '#52D6FC'; selectColor()"></div>
      <div class="main_color" style="background:#74A7FF" @click="selectedColor = '#74A7FF'; selectColor()"></div>
      <div class="main_color" style="background:#864FFD" @click="selectedColor = '#864FFD'; selectColor()"></div>
      <div class="main_color" style="background:#D357FE" @click="selectedColor = '#D357FE'; selectColor()"></div>
      <div class="main_color" style="background:#EE719E" @click="selectedColor = '#EE719E'; selectColor()"></div>
      <div class="main_color" style="background:#FF8C82" @click="selectedColor = '#FF8C82'; selectColor()"></div>
      <div class="main_color" style="background:#FEA57D" @click="selectedColor = '#FEA57D'; selectColor()"></div>
      <div class="main_color" style="background:#FEC777" @click="selectedColor = '#FEC777'; selectColor()"></div>
      <div class="main_color" style="background:#FED977" @click="selectedColor = '#FED977'; selectColor()"></div>
      <div class="main_color" style="background:#FFF994" @click="selectedColor = '#FFF994'; selectColor()"></div>
      <div class="main_color" style="background:#EAF28F" @click="selectedColor = '#EAF28F'; selectColor()"></div>
      <div class="main_color" style="background:#B1DD8B" @click="selectedColor = '#B1DD8B'; selectColor()"></div>
      <div class="main_color" style="background:#93E3FC" @click="selectedColor = '#93E3FC'; selectColor()"></div>
      <div class="main_color" style="background:#A7C6FF" @click="selectedColor = '#A7C6FF'; selectColor()"></div>
      <div class="main_color" style="background:#B18CFE" @click="selectedColor = '#B18CFE'; selectColor()"></div>
      <div class="main_color" style="background:#E292FE" @click="selectedColor = '#E292FE'; selectColor()"></div>
      <div class="main_color" style="background:#F4A4C0" @click="selectedColor = '#F4A4C0'; selectColor()"></div>
      <div class="main_color" style="background:#FFB5AF" @click="selectedColor = '#FFB5AF'; selectColor()"></div>
      <div class="main_color" style="background:#FFC5AB" @click="selectedColor = '#FFC5AB'; selectColor()"></div>
      <div class="main_color" style="background:#FED9A8" @click="selectedColor = '#FED9A8'; selectColor()"></div>
      <div class="main_color" style="background:#FDE4A8" @click="selectedColor = '#FDE4A8'; selectColor()"></div>
      <div class="main_color" style="background:#FFFBB9" @click="selectedColor = '#FFFBB9'; selectColor()"></div>
      <div class="main_color" style="background:#F1F7B7" @click="selectedColor = '#F1F7B7'; selectColor()"></div>
      <div class="main_color" style="background:#CDE8B5" @click="selectedColor = '#CDE8B5'; selectColor()"></div>
      <div class="main_color" style="background:#CBF0FF" @click="selectedColor = '#CBF0FF'; selectColor()"></div>
      <div class="main_color" style="background:#D2E2FE" @click="selectedColor = '#D2E2FE'; selectColor()"></div>
      <div class="main_color" style="background:#D8C9FE" @click="selectedColor = '#D8C9FE'; selectColor()"></div>
      <div class="main_color" style="background:#EFCAFE" @click="selectedColor = '#EFCAFE'; selectColor()"></div>
      <div class="main_color" style="background:#F9D3E0" @click="selectedColor = '#F9D3E0'; selectColor()"></div>
      <div class="main_color" style="background:#FFDAD8" @click="selectedColor = '#FFDAD8'; selectColor()"></div>
      <div class="main_color" style="background:#FFE2D6" @click="selectedColor = '#FFE2D6'; selectColor()"></div>
      <div class="main_color" style="background:#FEECD4" @click="selectedColor = '#FEECD4'; selectColor()"></div>
      <div class="main_color" style="background:#FEF1D5" @click="selectedColor = '#FEF1D5'; selectColor()"></div>
      <div class="main_color" style="background:#FDFBDD" @click="selectedColor = '#FDFBDD'; selectColor()"></div>
      <div class="main_color" style="background:#F6FADB" @click="selectedColor = '#F6FADB'; selectColor()"></div>
      <div class="main_color" style="background:#DEEED4" @click="selectedColor = '#DEEED4'; selectColor()"></div>
    </div>
    <div class="hex_container">
      <p>Указать HEX</p>
      <div class="pick">
        <input type="text" v-model="selectedColor" maxlength="7">
      </div>
    </div>
    <div class="divider"></div>
    <div class="current_container">
      <div class="current_color" :style="{ backgroundColor: selectedColor }"></div>
      <div class="colors">
        <div class="small_color"></div>
        <div class="small_color" style="background:#B08CFE"></div>
        <div class="small_color" style="background:#F188AE"></div>
        <div class="small_color" style="background:#5626C7"></div>
        <div class="small_color" style="background:#17014F"></div>
        <div class="small_color" style="background:#FFC25A"></div>
        <div class="small_color" style="background:#FF8C82"></div>
        <div class="small_color" style="background:#FF552F"></div>
        <div class="small_color" style="background:#FE7869"></div>
        <div class="plus_svg">
          <svg width="10" height="10" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z" fill="#D2D8DE"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
export default {
  data() {
    return {
      selectedColor: '#B08CFE',
    };
  },
  methods: {
    selectColor() {
      this.$emit('updateColor', this.selectedColor);
    }
  }
}
</script>

<style scoped>
.palitra{
  width: 320px;
  height: auto;
  background: #212326;
  border-radius: 5px;
  position: absolute;
  right: -100px;
  top: 40px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.palitra_container{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.circle_container{
  display: flex;
  justify-content: center;
}
.palitra_circle{
  width: 20px;
  height: 20px;
  border-radius: 25px;
  background: #33373D;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
p{
  font-family: TT Norms;
  font-size: 12px;
  font-weight: 500;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color: #FFFFFF;
  margin: 0;
}
.hex_container{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.pick{
  background: #33373D;  
  border-radius: 5px;
  color: #FFFFFF;
  width: auto;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.pick input{
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 500;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: center;
  color: #FFFFFF;
  margin: 0;
  padding: 0;
  height: auto;
  width: 80px;
  background-color: transparent;
}
.divider {
  border-bottom: 1px solid #33373D; 
  width: auto;
  margin: 0;
}
.current_container{
  display: flex;
  justify-content: space-between;
  gap: 15px;
}
.current_color{
  width: 40px;
  height: 40px;
  border-radius: 10px;
}
.colors{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 10px;
  align-items: center;
  justify-content: center;
}
.small_color{
  width: 15px;
  height: 15px;
  background:#6266EA;
  border-radius: 25px;
}
.palette{
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: repeat(10, 1fr);
  border-radius: 7px;
  overflow: hidden;
}
.main_color{
  width: auto;
  height: 24px;
  cursor: pointer;
  transition: all .2s ease;
}

.main_color:hover{
  filter: brightness(80%);
}
.plus_svg{
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>