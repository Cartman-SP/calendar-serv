<template>
  <div class="alert" :class="{ 'show': isVisible, 'hide': !isVisible }" :style="{ backgroundColor: color }">
    <p>{{ m }}</p>
    <div @click="hideNotification" style="display: flex; align-items: center; cursor: pointer;">
      <svg  width="8" height="8" viewBox="0 0 6 6" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M2.29294 3.00003L0.146484 5.14648L0.853591 5.85359L3.00004 3.70714L5.1465 5.85359L5.85361 5.14648L3.70715 3.00003L5.85359 0.853591L5.14648 0.146484L3.00004 2.29292L0.853605 0.146484L0.146499 0.853591L2.29294 3.00003Z" fill="white"/>
      </svg>
    </div>
    
  </div>
</template>

<script>
export default {
  props: ['message', 'color'],
  data() {
    return {
      isVisible: false,
      m: '',
      timeoutId: null
    };
  },
  watch: {
    message(newMessage) {
      if (newMessage) {
        this.updateNotification(newMessage);
      }
    }
  },
  methods: {
    updateNotification(newMessage) {
      this.hideNotification();
      setTimeout(() => {
        this.showNotification(newMessage);
      }, 300); // Небольшая задержка для плавного скрытия и показа
    },
    showNotification(newMessage) {
      this.m = newMessage;
      this.isVisible = true;
      if (this.timeoutId) {
        clearTimeout(this.timeoutId);
      }
      this.timeoutId = setTimeout(() => {
        this.hideNotification();
      }, 3000);
    },
    hideNotification() {
      this.isVisible = false;
      if (this.timeoutId) {
        clearTimeout(this.timeoutId);
        this.timeoutId = null;
      }
    }
  }
};
</script>

<style scoped>
.show {
  opacity: 100%;
  bottom: 20px;
  transition: all .2s ease;
}

.hide {
  opacity: 0;
  bottom: 0px;
  transition: all .2s ease;
}

svg:hover path{
    fill: rgb(214, 214, 214);
    cursor: pointer;
}
.alert{
  z-index: 100;
    padding: 10px 15px;
    position: absolute;
    width: fit-content;
    display: flex;
    gap: 20px;
    align-items: center;
    border-radius: 5px;
    left: 50%;
    transform: translateX(-50%);
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