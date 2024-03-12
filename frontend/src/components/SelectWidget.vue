<template>
  <div class="custom-select" :tabindex="tabindex" @blur="open = false" :id="colortheme">
    <div class="selected" :class="{ open: open }" @click="open = !open">
      {{ getOptionName(selected).length > 0 ? getOptionName(selected) : this.placeholderdata || options[0] }}
    </div>

    <div class="items" :class="{ selectHide: !open }">
      <div v-if="!optionsList.length > 0">Здесь пока ничего нет</div>
      <div
        v-for="option in optionsList"
        :key="getOptionKey(option)"
        @click="handleOptionClick(option)"
      >
        {{ getOptionName(option) }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    options: {
      required: true,
    },
    Theme: Boolean,
    MC: String,
    WC: String,
    BC: String,
    TC: String,
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
      selected: {},
      open: false,

      colortheme: '',
      MainColor: this.MC, // акцентный цвет виджета
      WidgetColor: this.WC, // цвет у фона
      BakcgroundColor: this.BC, // цвет у карточек
      TextColor: this.TC, // цвет текста
    };
  },
  computed: {
    optionsList() {
      if (Array.isArray(this.options)) {
        return this.options;
      } else if (typeof this.options === 'object') {
        return Object.keys(this.options).map(key => ({
          id: key,
          name: this.options[key]
        }));
      }
      return [];
    },
  },
  methods: {
    updateColors() {
      if (this.Theme) {
        this.colortheme = 'darkmode';
      } else {
        this.colortheme = 'lightmode';
      }

      if (this.MainColor) {
        this.$el.style.setProperty('--cm', this.MainColor);

        const transparentColor = this.changeTransparency(this.MainColor, 0.2);
        this.$el.style.setProperty('--cmlight', transparentColor);
      }
      if (this.WidgetColor) {
        this.$el.style.setProperty('--cw', this.WidgetColor);
      }
      if (this.BakcgroundColor) {
        this.$el.style.setProperty('--cb', this.BakcgroundColor);
      }
      if (this.TextColor) {
        this.$el.style.setProperty('--ct', this.TextColor);
      }
    },
    changeTransparency(hex, alpha) {
      const isValidHex = /^#([0-9A-Fa-f]{3}){1,2}$/i.test(hex);
      if (!isValidHex) {
        console.error('Invalid HEX color:', hex);
        return hex;
      }

      hex = hex.replace(/^#/, '');
      const bigint = parseInt(hex, 16);

      const r = (bigint >> 16) & 255;
      const g = (bigint >> 8) & 255;
      const b = bigint & 255;

      return `rgba(${r},${g},${b},${alpha})`;
    },



    handleOptionClick(option) {
      this.selected = option;
      this.open = false;
      this.$emit('input', option);
    },
    getOptionKey(option) {
      return option.id || option;
    },
    getOptionName(option) {
      return option && option.name !== undefined ? option.name : option;
    },
  },
  mounted() {
    if (this.optionsList.length > 0) {
      this.$emit("input", this.selected);
    }
  },
};
</script>


<style scoped>
#lightmode {
  --color-main: var(--cw, white);
  --color-gray: var(--cb, #FAFAFA);
  --color-btnmain: var(--cmlight, #EBEDFF);
  --color-global: var(--cm, #6266EA);
  --color-text: var(--ct, #535C69);
  --color-shadow: rgb(216, 216, 216);
}

#darkmode{
  --color-main: var(--cw, #1A1B27);
  --color-gray: var(--cb, #222433);
  --color-btnmain: var(--cmlight, rgba(255, 194, 90, 0.1));
  --color-global: var(--cm, #FFCF7D);
  --color-text: var(--ct, #F5F5F5);
  --color-shadow: rgb(21, 20, 29);
}

.custom-select {
  position: relative;
  width: 100%;
  text-align: left;
  outline: none;
  height: 24px;
  line-height: 36px;
  font-family: TT Norms light;
  font-size: 13px;
  border-radius: 3px;
}

.selected {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--color-main);
  color: var(--color-text);
  font-family: TT Norms light;
  font-size: 10px;
  font-weight: 300;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color: var(--color-text);
  width: 45px;
  height: 24px;
  cursor: pointer;
  border-radius: 3px;
  transition: all 0.2s ease;
}
.selected:hover{
  background: var(--color-global);
  color: var(--color-main);
}

.custom-select .selected.open {
  border-radius: 3px 3px 3px 3px;
}

.custom-select .items {
  width: 50px;
  font-size: 10px;
  max-height: 170px;
  overflow-y: scroll;
  margin-top: 10px;
  color: var(--color-text);
  border-radius: 3px 3px 3px 3px;
  position: absolute;
  background-color: var(--color-main);
  left: 0;
  right: 0;
  z-index: 1;
  filter: drop-shadow(0 0 10px var(--color-shadow));
}

.custom-select .items div {
  color: var(--color-text);
  padding: 0 10px;
  cursor: pointer;
  user-select: none;
}

.custom-select .items div:hover {
  background-color: var(--color-btnmain);
}

.selectHide {
  display: none;
}
</style>
