<template>
  <div class="main">
    <div class="content">
      <router-link to="/lk/project/new" class="add">
        <div class="svg-plus">
          <svg width="1em" height="1em" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z"/>
          </svg>            
        </div>
        <p>Создать проект</p>
      </router-link>
      <div v-for="project in allPProjects" :key="project.id">
        <CardProject :ProjectData="project"/>
      </div>
    </div>    
  </div>
</template>

<script>
import CardProject from '../components/CardProject.vue';
import axios from 'axios';

export default {
  components: { CardProject },
  data() {
        return {
            allPProjects:[],
        };
  },
  methods:{
    get_projects(){
      axios.get('http://sked.online/api/create_project/', {
        params: {
          user_id: this.$store.state.registrationData.user_id // Замените на нужный вам user_id
        }
      })
      .then(response => {
        console.log(response)
        this.allPProjects = response.data
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
  },
  mounted(){
    this.get_projects();
  },
}
</script>

<style scoped>
.content{
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(4, 1fr);
  margin-right: 50px;
}
.add {
  text-decoration-line: initial;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  display: flex;
  height: 100%;
  gap: 10px;
  width: 100%;
  color: #6266EA;
  border-style: dashed;
  border-width: 2px;
  border-color: #D9D9D9;
  transition: 0.3s ease;
  padding: 20px;
  border-radius: 5px;
}
.svg-plus{
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 40px;
  width: 1em;
  height: 1em;
}
p{
  margin: 0;
}
.add:hover{
  background: #EFEFFF;
}
</style>