<template>
  <div>
    <div>
        <label for="serviceCover" class="file-label">Обложка услуги</label>
        <label class="custom-file-upload" :class="{'custom-file-upload-error' : serviceCoverError}" v-if="!fileNameVariable">
            <input type="file" accept="image/*" @change="handleFileUpload($event)"/>Нажмите, чтобы добавить 
          </label>
          <label style="color: #535C69;" class="custom-file-upload" :class="{'custom-file-upload-error' : serviceCoverError}" v-else>
            <input type="file" accept="image/*" @change="handleFileUpload($event)"/>{{ fileNameVariable }}
          </label>
        <p class="text">до 5 МБ, PNG, JPG, JPEG</p>
      </div>
  </div>
  
</template>

<script>
export default {
data() {
    return {
        firstname: 'Daniil',
        secondname: 'Shirkin',
        mail: 'Daniil.shirkin005@gmail.com',
        phone: '79672262425',
        date: '24.06.2005',
        serviceCover: ''
    }
},

methods:{
    create_client(){
        const formData = new FormData();
        formData.append('firstname', this.firstname);
        formData.append('secondname', this.secondname);
        formData.append('mail', this.mail);
        formData.append('img', this.serviceCover);
        formData.append('phone', this.phone)
        formData.append('date', this.date)
        axios.post('http://127.0.0.1:8000/api/uslugi/', formData)
        .then(response => {
          console.log('Service created:', response.data); // ЧИТАЙТЕ КОММЕНТАРИЙ ЗДЕСЬ ВОЗВРАЩАЕТСЯ True или False со значением надо ли показывать модалку о первом создании услуги!!!!!!!!!!!!!
          this.alertMessage = 'Настройки успешно сохранены'
          this.alertColor = '#0BB6A1'
          if(response.data){
          this.first = response.data
          }else{
          setTimeout(() => {
            this.$router.push('/dashboard/service');
          }, 2000)}
        })
        .catch(error => {
          console.error('Error creating service:', error);
        });
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      this.serviceCover = file; // сохраняем весь объект файла
      this.create_client()
    },
},
mounted:{

}
}
</script>

<style>

</style>