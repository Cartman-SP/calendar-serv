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
      delete_widget() {
        let id = 1
        const formData = new FormData();
        formData.append('id', id);
        axios.post('http://127.0.0.1:8000/api/delete_widget/', formData)
          .then(response => {
            console.log('application deleted:', response.data);
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
    async get_busytime(){
      try {
        let employee_id = this.employee_id 
        const response = await axios.get(`http://127.0.0.1:8000/api/get_widgetid/?employee_id=${employee_id}`);
        console.log(response.data.id)
      } catch (error) {
        console.error('Error fetching applications:', error);
      }
    },
    async getusluga(i) {
        try {
            const id = i;
            const response = await axios.get(`http://127.0.0.1:8000/api/get_uslugabyid/?variable=${id}`);
            console.log(response)
            return response.data;
        } catch (error) {
            console.error('Ошибка при получении данных о Услуге:', error);
            throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
        }
    },
    async getemployee(i) {
        try {
            const id = i;
            const response = await axios.get(`http://127.0.0.1:8000/api/get_employeebyid/?variable=${id}`);
            console.log(response)
            return response.data;
        } catch (error) {
            console.error('Ошибка при получении данных о Сотруднике:', error);
            throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
        }
    },
    async getfilial(i) {
        try {
            const id = i;
            const response = await axios.get(`http://127.0.0.1:8000/api/get_filialbyid/?variable=${id}`);
            console.log(response)
            return response.data;
        } catch (error) {
            console.error('Ошибка при получении данных о Филиале:', error);
            throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
        }
    },
    async getclient(i) {
        try {
            const id = i;
            const response = await axios.get(`http://127.0.0.1:8000/api/get_clientbyid/?variable=${id}`);
            console.log(response)
            return response.data;
        } catch (error) {
            console.error('Ошибка при получении данных о Клиенте:', error);
            throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
        }
    },

    async get_time(){
        try {
          let dayofWeek = 'Ср'
          let employee_id = 1
          let usluga_id = 1
          const response = await axios.get(`http://127.0.0.1:8000/api/get_time/?employee_id=${employee_id}&usluga_id=${usluga_id}&dayofWeek=${dayofWeek}`);
          console.log(response.data)
        } catch (error) {
          console.error('Error fetching applications:', error);
        }
      },
    
    
    
    
    
    async editUsluga(uslugaId, updatedData) 
    {
      try 
      {
        const response = await axios.patch(`http://127.0.0.1:8000/api/usluga/${uslugaId}/edit/`, updatedData);
        console.log(response.data);
        return response.data;
      }
      catch (error) 
      {
        console.error('Error editing usluga:', error);
        throw error;
      }
    },

    async editEmployee(employeeId, updatedData) 
    {
      try 
      {
        const response = await axios.patch(`http://127.0.0.1:8000/api/employee/${employeeId}/edit/`, updatedData);
        console.log(response.data);
        return response.data;
      }
      catch (error) 
      {
        console.error('Error editing employee:', error);
        throw error;
      }
    },

    async  editBranch(branchId, updatedData) 
    {
      try 
      {
        const response = await axios.patch(`http://127.0.0.1:8000/api/branch/${branchId}/edit/`, updatedData);
        console.log(response.data);
        return response.data;
      }
      catch (error) 
      {
        console.error('Error editing branch:', error);
        throw error;
      }
    },

    async editWidget(widgetId, updatedData) 
    {
      try 
      {
        const response = await axios.patch(`http://127.0.0.1:8000/api/widget/${widgetId}/edit/`, updatedData);
        console.log(response.data);
        return response.data;
      }
      catch (error) 
      {
        console.error('Error editing widget:', error);
        throw error;
      }
    },
    async  createApplicationFromWidget(applicationData) 
    {
      try 
      {
        const response = await axios.post('http://127.0.0.1:8000/api/create_application_from_widget/', {
            application: applicationData
        });
        console.log(response.data);
        return response.data;
      }
      catch (error) 
      {
        console.error('Error creating application from widget:', error);
        throw error;
      }
    },
    async  getEarnings(period) 
    {
      try 
      {
        const response = await axios.get(`http://127.0.0.1:8000/api/earnings/?period=${period}`);
        console.log(response.data);
        return response.data;
      }
      catch (error) 
      {
        console.error('Error fetching earnings:', error);
        throw error;
      }
    }


    },
    mounted() {
      this.get_time()

    }
  };
  </script>
  
  <style scoped>
  /* Your CSS styles */
  </style>
  