<template>
  <div class="arts-detail-card">
    <div
      class="arts-detail-icon-container"
      :style="'background-color:' + color"
    >
      <img
        v-if="arttype.toLowerCase() === 'grants'"
        src="@/assets/images/resource_icon.svg"
        alt="Arts"
      />
    </div>

    <div class="arts-detail-text">
      <div>
        <h5 class="field-kind">
          {{ arttype | kind }}
        </h5>
        <h5 class="field-name">
          {{ name }}
        </h5>
      </div>
      <div class="artist-tags-container">
        <span v-for="tag in tags" :key="`grants-tag-${tag}`">{{ tag }}</span>
      </div>
    </div>

    <div class="fpcc-card-more-art" @click.prevent="handleReturn">
      <img
        v-if="hover"
        class="ml-1"
        src="@/assets/images/return_icon.svg"
        alt="Go"
      />
      <img
        v-else
        class="ml-1"
        src="@/assets/images/return_icon_hover.svg"
        alt="Go"
      />
      <span class="ml-1 font-weight-bold">Return</span>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  filters: {
    kind(d) {
      if (d === 'public_art') {
        return 'Public Art'
      }
      return d
    }
  },
  props: {
    name: {
      type: String,
      default: ''
    },
    color: {
      type: String,
      default: 'RGB(255, 255, 255)'
    },
    arttype: {
      type: String,
      default: 'Public Art'
    },
    tags: {
      type: Array,
      default: () => {
        return {}
      }
    }
  },
  data() {
    return {
      hover: false
    }
  },
  methods: {
    handleReturn() {
      this.$root.$emit('resetMap')
      this.$store.commit('sidebar/setDrawerContent', false)
      this.$router.push({
        path: '/grants'
      })
    }
  }
}
</script>

<style lang="scss">
.arts-detail-card {
  border-bottom: 3px solid #f9f9f9;
  display: flex;
  justify-content: flex-start;
  width: 100%;
  border: 1px solid #ebe6dc;
  padding: 1em 0 1em 1em;
  border-radius: 0.25em;
  position: relative;
}
.arts-detail-icon-container {
  background-color: black;
  border-radius: 50%;
  height: 50px;
  width: 50px;
}

.arts-detail-text {
  margin-left: 0.5em;
  width: 65%;
}
.arts-detail-icon-container img {
  display: inline-block;
  width: 100%;
  height: 100%;
}
.fpcc-card-more-art {
  cursor: pointer;
  width: 90px;
  background-color: #b47a2b;
  height: 35px;
  border-top-left-radius: 1em;
  border-bottom-left-radius: 1em;
  color: #fff;
  z-index: 50000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1em;
  position: absolute;
  right: 0;
  top: 25%;
}

.fpcc-card-more-art:hover {
  color: white;
  background-color: #454545;
}

.fpcc-card-more-art img {
  display: inline-block;
  width: 15px;
  height: 15px;
}

.fpcc-card {
  border: 0;
  box-shadow: none;
}

.field-kind {
  font: Bold 15px/18px Proxima Nova;
  color: #707070;
  opacity: 1;
  text-transform: uppercase;
  margin: 0.1em;
  padding: 0;
}

.field-name {
  font: Bold 16px/20px Proxima Nova;
  color: #151515;
  margin: 0.1em;
  padding: 0;
  letter-spacing: 0.5px;
  width: 95%;
}

.artist-tags-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: center;
}

.artist-tags-container span {
  cursor: pointer;
  flex: 0 1 auto;
  background: #ddd4c6;
  border-radius: 2rem;
  color: #707070;
  text-transform: uppercase;
  font: Bold 12px Proxima Nova;
  margin: 0.25em 0.5em 0.25em 0;
  padding: 2px 5px;
  text-align: center;

  &:hover {
    color: #fff;
    background-color: #545b62;
  }
}
</style>
