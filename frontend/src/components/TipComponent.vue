<template>
    <div style="display: flex; flex-direction: column; align-items: center;">
        <svg
        width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"
        @mouseover="showTooltip" @mouseleave="hideTooltip">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M13.5 6.75C13.5 10.4779 10.4779 13.5 6.75 13.5C3.02208 13.5 0 10.4779 0 6.75C0 3.02208 3.02208 0 6.75 0C10.4779 0 13.5 3.02208 13.5 6.75ZM6 4.5C6 4.25228 6.08982 4.11237 6.19889 4.02148C6.32516 3.91625 6.52224 3.84375 6.75 3.84375C6.97775 3.84375 7.17483 3.91625 7.30111 4.02148C7.41018 4.11237 7.5 4.25229 7.5 4.5C7.5 4.74377 7.44122 4.87673 7.39159 4.95117C7.33883 5.0303 7.26312 5.09242 7.16459 5.14168C7.06313 5.19241 6.95258 5.22152 6.86108 5.23677C6.83485 5.24114 6.79675 5.24503 6.77025 5.24745L6.7486 5.25L6.75 5.25C6.55394 5.25206 6.35846 5.33088 6.21967 5.46967C6.07902 5.61032 6 5.80109 6 6V7.5H7.5V6.62052C7.60694 6.5856 7.72037 6.54084 7.83541 6.48332C8.11188 6.34509 8.41117 6.12596 8.63966 5.78322C8.87129 5.43578 9 5.00624 9 4.5C9 3.81022 8.71482 3.24701 8.26139 2.86915C7.82517 2.50563 7.27225 2.34375 6.75 2.34375C6.22776 2.34375 5.67484 2.50562 5.23861 2.86914C4.78518 3.247 4.5 3.81021 4.5 4.5H6ZM6.75 8.625C6.12868 8.625 5.625 9.12868 5.625 9.75C5.625 10.3713 6.12868 10.875 6.75 10.875C7.37132 10.875 7.875 10.3713 7.875 9.75C7.875 9.12868 7.37132 8.625 6.75 8.625Z" fill="#535C69"/>
        </svg>
  
        <div v-if="isTooltipVisible" class="tooltip show">
          <div class="tooltip-content" v-html="formattedTip" :style="{ minWidth: Width }">
        </div>
      <div class="tooltip-arrow"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['Tip', 'Width'],
  data() {
    return {
      isTooltipVisible: false,
    };
  },
  methods: {
    showTooltip() {
      this.isTooltipVisible = true;
    },
    hideTooltip() {
      this.isTooltipVisible = false;
    },
  },
  computed: {
    formattedTip() {
      return this.Tip.replace(/\n/g, '<br>').replace(/<span>/g, '<span style="font-family: TT Norms Light;">');
    }
  },
};
</script>
  
  <style scoped>
  span {
    color: red;
  }
  .tooltip-content{
    font-family: 'TT Norms Medium';
    font-size: 15px;
  }

  svg{
    position: relative;
    display: inline-block;
  }
  .tooltip {
    max-width: 700px;
    width: auto;
    text-align: left;
  transform: translateY(22px);
  word-wrap: break-word;
  overflow-wrap: break-word;
  position: absolute;
  background-color: #212326;
  color: #fff;
  padding: 10px;
  border-radius: 5px;
  position: absolute;
  z-index: 999;
  opacity: 0;
  transition: opacity .2s ease;
}

.tooltip.show {
  opacity: 1;
}
  
  .tooltip-arrow {
    position: absolute;
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-bottom: 5px solid #212326;
    top: -5px;
    left: 50%;
    transform: translateX(-50%);
  }

svg path{
    fill: #AFB6C1;
}

svg:hover path{
    fill: #535C69;
}

</style>