<template>
  <div class="custom-select" :tabindex="tabindex" @blur="open = false">
    <div class="selected" :class="{ open: open }" @click="open = !open">
      {{ selected }}
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
  },
  data() {
    return {
      selected: this.default
        ? this.default
        : this.options && this.options.length > 0
        ? this.options[0]
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

.custom-select .selected {
  background-color: #F3F5F6;
  border-radius: 3px;
  color: #535C69;
  padding-left: 1em;
  cursor: pointer;
  user-select: none;
}

.custom-select .selected.open {
  border-radius: 6px 6px 0px 0px;
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
  color: #535C69;
  border-radius: 0px 0px 6px 6px;
  overflow: hidden;
  position: absolute;
  background-color: #FFFFFF;
  left: 0;
  right: 0;
  z-index: 1;
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
