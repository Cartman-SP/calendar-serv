<template>
    <div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        firstname: 'Daniil',
        secondname: 'Shirkin',
        mail: 'Daniil.shirkin005@gmail.com',
        phone: '79672262425',
        date: '24.06.2005',
        serviceCover: '',
        fileNameVariable: '',
        serviceCoverError: false,
        data: '24.06.2005',
        usluga_id: 1,
        employee_id: 1,
        client_id: 1,
        project_id: 1,
        branch_id: 1,
        request_id:2,
      };
    },
    methods: {
      create_client() {
        const formData = new FormData();
        formData.append('firstname', this.firstname);
        formData.append('secondname', this.secondname);
        formData.append('mail', this.mail);
        formData.append('phone', this.phone);
        formData.append('date', this.date);
        formData.append('project', this.project_id);
        axios.post('http://127.0.0.1:8000/api/create_client/', formData)
          .then(response => {
            console.log('Service created:', response.data);
          })
          .catch(error => {
            console.error('Error creating service:', error);
          });
      },
      create_application() {
        const formData = new FormData();
        formData.append('status', this.status);
        formData.append('data', this.data);
        formData.append('usluga', this.usluga_id);
        formData.append('employee', this.employee_id);
        formData.append('client', this.client_id);
        formData.append('project', this.project_id);
        formData.append('branch',this.branch_id);
        formData.append('time', this.time) /// 2024-06-15T10:30:00.000Z
        axios.post('http://127.0.0.1:8000/api/create_applications/', formData)
          .then(response => {
            console.log('application created:', response.data);
          })
          .catch(error => {
            console.error('Error creating application:', error);
          });
      },
      async get_applications(){
      try {
        let project_id = this.project_id 
        const response = await axios.get(`http://127.0.0.1:8000/api/get_applications/?project=${project_id}`);
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching applications:', error);
      }
    },
    
    async get_applications(){
      try {
        let project_id = this.project_id 
        const response = await axios.get(`http://127.0.0.1:8000/api/get_applications/?project=${project_id}`);
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching applications:', error);
      }
    },

    async get_client(){
      try {
        let project_id = this.project_id 
        const response = await axios.get(`http://127.0.0.1:8000/api/get_client/?project=${project_id}`);
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching clients:', error);
      }
    },
    async get_integration(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/get_integration/`);
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching integrations:', error);
      }
    },
    async get_widgetid(){
      try {
        let name = this.widgetname 
        const response = await axios.get(`http://127.0.0.1:8000/api/get_widgetid/?widgetname=${name}`);
        console.log(response.data.id)
      } catch (error) {
        console.error('Error fetching applications:', error);
      }
    },


      
    },
    mounted() {
      this.create_application()
      this.get_request(1,1)
      this.delete_request()
        console.log('Component mounted')
      this.get_applications();
    }
  };
  </script>
  
  <style scoped>
  /* Your CSS styles */
  </style>
  