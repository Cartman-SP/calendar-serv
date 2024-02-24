<template>
  <div class="custom-select" :tabindex="tabindex" @blur="open = false">
    <div class="selected" :class="{ open: open, placeholder: !selected }" @click="open = !open">
      {{ selected ? selected : this.placeholderdata || 'Укажите плейсхолдер' }}
    </div>
    <div class="items" :class="{ selectHide: !open }">
      <div
        v-for="(option, i) of options"
        :key="i"
        @click="
          selected = option;
          open = false; 
          $emit('input', option);
        "
      >
        {{ option }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    options: {
      type: Array,
      required: true,
    },
    default: {
      type: String,
      required: false,
      default: null,
    },
    tabindex: {
      type: Number,
      required: false,
      default: 0,
    },
    placeholderdata: {
      type: String,
    },
  },
  data() {
    return {
      selected: this.default
        ? this.default
        : null,
      open: false,
    };
  },
  mounted() {
    if (this.options && this.options.length > 0) {
      this.$emit("input", this.selected);
    }
  },
};
</script>

<style scoped>
.custom-select {
  position: relative;
  width: 100%;
  text-align: left;
  outline: none;
  height: 36px;
  line-height: 36px;
  font-family: TT Norms Medium;
  font-size: 12px;
}

.custom-select .selected.placeholder {
  color: #D2D8DE; /* Красный цвет для placeholder */
}

.custom-select .selected {
  background-color: #F3F5F6;
  border-radius: 5px;
  color: #535C69;
  padding-left: 1em;
  cursor: pointer;
  user-select: none;
}

.custom-select .selected.open {
  border-radius: 5px 5px 5px 5px;
}

.custom-select .selected:after {
  position: absolute;
  content: "";
  top: 16px;
  right: 1em;
  width: 0;
  height: 0;
  border: 5px solid transparent;
  border-color: #535C69 transparent transparent transparent;
}

.custom-select .items {
  margin-top: 10px;
  color: #535C69;
  border-radius: 5px 5px 5px 5px;
  overflow: hidden;
  position: absolute;
  background-color: #FFFFFF;
  left: 0;
  right: 0;
  z-index: 1;
  filter: drop-shadow(0 0 10px rgb(227, 227, 227));
}

.custom-select .items div {
  color: #535C69;
  padding-left: 1em;
  cursor: pointer;
  user-select: none;
}

.custom-select .items div:hover {
  background-color: #F3F5F6;
}

.selectHide {
  display: none;
}
</style>
