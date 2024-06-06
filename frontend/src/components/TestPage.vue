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
        status: 'Done',
        data: '24.06.2005',
        usluga_id: 1,
        employee_id: 1,
        client_id: 1,
        project_id: 1,
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
        axios.post('http://127.0.0.1:8000/api/create_applications/', formData)
          .then(response => {
            console.log('Service created:', response.data);
          })
          .catch(error => {
            console.error('Error creating service:', error);
          });
      },
      async get_applications(){
      try {
        let project_id = this.project_id 
        const response = await axios.get(`http://127.0.0.1:8000/api/get_applications/?project=${project_id}`);
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
    async get_client(){
      try {
        let project_id = this.project_id 
        const response = await axios.get(`http://127.0.0.1:8000/api/get_client/?project=${project_id}`);
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
    async get_integration(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/get_integration/`);
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },

    },
    mounted() {
        this.create_client()
        this.create_application()
        this.get_applications()
        this.get_client()
        this.get_integration()
        console.log('Component mounted');
    }
  };
  </script>
  
  <style>
  /* Your CSS styles */
  </style>
  