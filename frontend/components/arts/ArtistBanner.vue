<template>
  <div class="arts-artist-banner">
    <div class="arts-artist-header">
      <slot name="header"></slot>
    </div>
    <div class="arts-artist-body"><slot name="body"></slot></div>
  </div>
</template>

<script>
export default {
  props: {
    variant: {
      default: 'normal',
      type: String
    }
  }
}
</script>

<style>
.arts-artist-banner {
  margin-bottom: 0.5em;
}

.arts-artist-header {
  position: relative;
  border-bottom: 0.8px solid rgb(0, 0, 0, 0.25);
  margin-bottom: 55px;
  display: flex;
  justify-content: center;
}

.arts-artist-body {
  width: 100%;
  position: relative;
}

@media (max-width: 992px) {
  .arts-artist-banner {
    border-radius: 5px;
    background: #ffffff 0% 0% no-repeat padding-box;
    border: 1px solid #dedee4;
  }
  .arts-artist-header {
    border-top-left-radius: 5px;
  }
}
</style>
