<template>
  <div class="palitra">
    <div class="palitra_container">
      <div class="svg_container">
        <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M15.5 13C15.2889 13.3561 15.0922 13.6724 14.9095 13.9563C14.578 14.4713 14.2924 14.8796 14.0507 15.2253C13.3313 16.2542 13 16.7279 13 17.8058C13 19.4455 14.3445 20 15.5 20C16.6556 20 18 19.4455 18 17.8058C18 16.7279 17.6687 16.2541 16.9493 15.2253C16.7076 14.8796 16.422 14.4713 16.0905 13.9563C15.9078 13.6724 15.7111 13.3561 15.5 13ZM15.5 14.8791C15.2459 15.2618 15.02 15.5853 14.8315 15.8553C14.6723 16.0833 14.5397 16.2731 14.4395 16.428C14.2565 16.7108 14.1571 16.9049 14.0962 17.0887C14.0376 17.2656 14 17.4786 14 17.8058C14 18.3081 14.1845 18.5515 14.3983 18.7043C14.659 18.8907 15.0592 19 15.5 19C15.9408 19 16.341 18.8907 16.6017 18.7043C16.8155 18.5515 17 18.3081 17 17.8058C17 17.4786 16.9624 17.2656 16.9038 17.0887C16.8429 16.9049 16.7435 16.7108 16.5605 16.428C16.4603 16.2731 16.3277 16.0833 16.1685 15.8553C15.98 15.5853 15.7541 15.2618 15.5 14.8791Z" fill="white"/>
          <path fill-rule="evenodd" clip-rule="evenodd" d="M0 11.6739C6.30924e-05 11.8455 0.0394801 12.0171 0.118251 12.1735C0.168734 12.2738 0.235381 12.3679 0.318191 12.4518L6.46364 18.6776C6.88789 19.1075 7.57575 19.1075 8 18.6776L15.6818 10.8953C16.1061 10.4655 16.1061 9.76863 15.6818 9.33882L6.46364 0L5.69546 0.665295L8 3L0.318191 10.8953C0.23538 10.9792 0.168733 11.0733 0.11825 11.1735C0.0394799 11.33 6.30922e-05 11.5024 0 11.6739ZM1.44866 12.1735L7.17533 17.9751C7.20803 18.0083 7.25561 18.0083 7.28831 17.9751L13.015 12.1735H1.44866ZM14.0021 11.1735H1.4427L8.71245 3.70175L14.9701 10.0413C14.9888 10.0602 15 10.0857 15 10.1171C15 10.1484 14.9888 10.1739 14.9701 10.1928L14.0021 11.1735Z" fill="white"/>
        </svg>  
      </div>
      <p class="">Основной цвет</p>
      <div class="circle_container">
        <div class="palitra_circle"></div>
      </div>
    </div>
    <div class="hex_container">
      <p>Указать HEX</p>
      <div class="pick">
        <p>#6266EA</p>
      </div>
    </div>
    <div class="divider"></div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.palitra{
  width: 200px;
  height: 270px;
  background: #212326;
  border-radius: 5px;
  position: absolute;
  padding: 10px;
}
.palitra_container{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.circle_container{
  display: flex;
  justify-content: center;
}
.palitra_circle{
  width: 12px;
  height: 12px;
  border-radius: 25px;
  background: #33373D;
}
p{
  font-family: TT Norms;
  font-size: 8px;
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
}
.pick{
  background: #33373D;  
  border-radius: 5px;
  color: #FFFFFF;
  width: 60px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.divider {
  border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
  width: auto;
  margin: 20px 0;
}
</style>