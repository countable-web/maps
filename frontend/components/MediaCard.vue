<template>
  <div
    class="artist-card"
    @mouseover.prevent="handleMouseOver"
    @mouseleave="handleMouseLeave"
  >
    <!-- Render if Media -->
    <div v-if="isMedia" class="arts-card-landscape">
      <div class="arts-card-body">
        <img
          v-lazy="artImage"
          :class="`card-teaser-img ${mediaExist ? '' : 'card-teaser-null'}`"
        />
      </div>
      <div class="arts-card-right">
        <div class="arts-card-footer">
          <span class="artist-title"> {{ media.name }} </span>
        </div>
        <div class="arts-card-more">
          <div class="arts-card-tag">
            <img :src="returnMediaTypeLogo" />
            {{ media.file_type }}
          </div>
          <div class="fpcc-card-more">
            <img
              v-if="!hover"
              src="@/assets/images/go_icon_hover.svg"
              alt="Go"
            />
            <img v-else src="@/assets/images/go_icon_hover.svg" alt="Go" />
          </div>
        </div>
      </div>
    </div>
    <!-- Render if Public Art -->
    <div v-else class="arts-card-landscape">
      <div class="arts-card-body">
        <img v-lazy="getMediaUrl(media.image)" :class="`card-teaser-img`" />
      </div>
      <div class="arts-card-right">
        <div class="arts-card-footer">
          <span class="artist-title"> {{ media.name }} </span>
        </div>
        <div class="arts-card-more">
          <div class="arts-card-tag">
            <img src="@/assets/images/arts/image.png" />
            Public Art
          </div>
          <div class="fpcc-card-more">
            <img
              v-if="!hover"
              src="@/assets/images/go_icon_hover.svg"
              alt="Go"
            />
            <img v-else src="@/assets/images/go_icon_hover.svg" alt="Go" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getMediaUrl } from '@/plugins/utils.js'
export default {
  props: {
    media: {
      type: Object,
      default: () => {
        return {}
      }
    },
    geometry: {
      type: Object,
      default: () => {
        return {}
      }
    },
    type: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      hover: false
    }
  },
  computed: {
    isMedia() {
      return this.type === 'media'
    },
    videoThumbnail() {
      return `https://img.youtube.com/vi/${this.getYoutubeVideoID(
        this.media.url
      )}/hqdefault.jpg`
    },
    artImage() {
      return this.mediaExist
        ? getMediaUrl(this.media.media_file)
        : this.media.file_type === 'video'
        ? this.videoThumbnail
        : require('@/assets/images/public_art_icon.svg')
    },
    returnMediaTypeLogo() {
      const type = this.media.file_type ? this.media.file_type : 'audio'
      return require(`@/assets/images/arts/${type}.png`)
    },
    mediaExist() {
      return this.media.media_file !== null
    }
  },
  methods: {
    getMediaUrl,
    handleMouseOver() {
      this.hover = true
      // in some cases, we list places without full geometry, no marker shown.
      if (!this.geometry) return
      this.$eventHub.revealArea(this.geometry)
    },
    handleMouseLeave() {
      this.hover = false
      // in some cases, we list places without full geometry, no marker shown.
      if (!this.geometry) return
      this.$eventHub.doneReveal()
    },
    onImageError(event) {
      event.target.src = '@/assets/images/public_art_icon.svg'
    },
    getYoutubeVideoID(url) {
      const regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/
      const match = url.match(regExp)
      return match && match[7].length === 11 ? match[7] : false
    }
  }
}
</script>

<style lang="scss">
.arts-card-landscape {
  background-color: #fff;
}
</style>