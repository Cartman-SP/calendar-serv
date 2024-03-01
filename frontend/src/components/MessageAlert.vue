<template>
    <div v-if="isVisible" class="alert" :style="{ backgroundColor: color }">
      <p>{{ message }}</p>
      <svg @click="isVisible = false" width="8" height="8" viewBox="0 0 6 6" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M2.29294 3.00003L0.146484 5.14648L0.853591 5.85359L3.00004 3.70714L5.1465 5.85359L5.85361 5.14648L3.70715 3.00003L5.85359 0.853591L5.14648 0.146484L3.00004 2.29292L0.853605 0.146484L0.146499 0.853591L2.29294 3.00003Z" fill="white"/>
      </svg>
    </div>
</template>
  
  <script>
  export default {
    props: {
      message: String,
      color: String,
    },
    data() {
      return {
        isVisible: false,
      };
    },
    mounted() {
      this.showNotification();
    },
    methods: {
      showNotification() {
        this.isVisible = true;
        setTimeout(() => {
          this.isVisible = false;
        }, 7000); // 7 seconds
      },
    },
  };
  </script>
  
  

<style scoped>

svg:hover path{
    fill: rgb(214, 214, 214);
    cursor: pointer;
}
.alert{
    /* background-color: #0BB6A1; */
    padding: 10px 15px;
    position: absolute;
    bottom: 10px;
    width: fit-content;
    display: flex;
    gap: 20px;
    align-items: center;
    border-radius: 5px;
    left: 50%;
    transform: translateX(-50%);
    transition: all .2s ease;
}

.alert p{
    margin: 0;
    margin-top: -2px;
    color: white;
    font-family: 'TT Norms Medium';
    font-size: 14px;
}

svg path{
    fill: white;
}
</style>