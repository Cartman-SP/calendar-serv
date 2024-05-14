<template>
  <div class="clients">
    <p class="head">Клиенты</p>
    <div class="clients_main">
      <div class="add">
        <div class="delete">
          <img src="../../static/img/dell.svg" alt="">
        </div>
        <button class="client_add" @click="this.$router.push('/dashboard/clients/create')">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z" fill="#6266EA"/>
          </svg>
          Добавить клиента</button>
      </div>
      <div class="people">
        <div class="people_nav">
          <div class="status">
            <div class="mark" v-if="!Mark" @click="Mark = true"></div>
            <div class="mark_active" v-else @click="Mark = false">
              <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#FFFFFF"/>
              </svg>
            </div>
            <p class="people_nav_text">Email</p>
          </div>
          <p class="people_nav_text">Добавлен</p>
          <p class="people_nav_text">Телефон</p>
          <p class="people_nav_text">Действия</p>
        </div>
        <div class="divider"></div>
        <div class="people_main">
          <div class="checkmark">
            <div class="mark" v-if="!Mark" @click="Mark = true"></div>
            <div class="checkmark_active" v-else @click="Mark = false">
              <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#FFFFFF"/>
              </svg>
            </div>
            <div class="people_container">
              <img src="../../static/img/data.png" alt="" class="circle">
              <div class="cont">
                <div class="wrapper">
                  <p class="people_head" @click="this.$router.push('/dashboard/clients/edit')">Никита Половинко</p>
                  <img class="edit" src="../../static/img/discover.svg" alt="" @click="this.$router.push('/dashboard/clients/edit')">
                </div>
                <p class="people_nav_texts" @click="this.$router.push('/dashboard/clients/edit')">nikitapolovinko@gmail.com</p>
              </div>
            </div>
          </div>
          <p class="people_nav_text">29.04.2024 , 10:49</p>
          <div class="copy">
            <p class="people_nav_text">+7 707 877 35 78</p>
            <img src="../../static/img/copy.svg" alt="">
          </div>
          <div class="keys">
            <img src="../../static/img/cog.svg" alt="" class="">
            <img src="../../static/img/delete.svg" alt="" class="">
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
      Mark: false,
    }
  },

}
</script>

<style scoped>
.head{
  font-family: TT Norms Medium;
  font-size: 20px;
  line-height: 23.6px;
  text-align: left;
  color: #535C69;
}
.clients{
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.clients_main{
  height: auto;
  background: #FFFFFF;
  padding: 20px;
  border-radius: 5px;
  width: 70%;
  display: flex;
  flex-direction: column;
  gap: 40px;
}
.delete{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border-radius: 3px;
  border: 1px solid #F3F5F6;
}
.add{
  display: flex;
  justify-content: space-between;
}
.client_add{
  background: #EFEFFF;
  color: #6266EA;
  transition: all 0.3s ease;
}
.client_add:hover{
  background: #464AD9;
  color: #FFFFFF;
}
.status{
  display: flex;
  gap: 50px;
}
.mark{
  width: 16px;
  height: 16px;
  border-radius: 3px;
  border: 1px solid #C6CBD2;
  cursor: pointer;
  user-select:none;
}
.mark_active{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 16px;
  height: 16px;
  border-radius: 3px;
  border: 1px solid #C6CBD2;
  cursor: pointer;
  background: #6266EA;
  user-select:none;
}
.people_nav_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #7D838C;
  display: flex;
  align-items: center;
  justify-content: center;
}
.people_nav_texts{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #7D838C;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.people_nav{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 1fr;
}
.people_main{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 1fr;  
}
p{
  margin: 0;
}
.divider {
  border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
  width: auto;
  margin: 10px 0;
  margin-bottom: 40px;
}
.checkmark_active{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 16px;
  height: 16px;
  border-radius: 3px;
  border: 1px solid #C6CBD2;
  cursor: pointer;
  background: #6266EA;
  user-select:none;
}
.people_head{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #535C69;
  cursor: pointer;
}
.checkmark{
  display: flex;
  align-items: center;
  gap: 50px;
}
.wrapper{
  display: flex;
  gap: 5px;
}
.people_container{
  display: flex;
  gap: 10px;
}
.circle{
  width: 32px;
  height: 32px;
  border-radius: 30px;
}
.copy{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}
.keys{
  display: flex;
  gap: 10px;
  justify-content: center;
  align-items: center;
}
.edit{
  cursor: pointer;
}
</style>