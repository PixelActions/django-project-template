from djangoseo import seo

def default_title(metadata, model_instance=None, **kwargs):
    return "Default website title"

def default_keywords(metadata, model_instance=None, **kwargs):
    return "Default site keywords"

def default_description(metadata, model_instance=None, **kwargs):
    return "Default page descsription."

def default_image(metadata, model_instance=None, **kwargs):
    return "Default Image to show when FB Sharing page"


class BasicMetadata(seo.Metadata):
    title = seo.Tag(max_length=68, head=True, populate_from=default_title)
    keywords = seo.KeywordTag(populate_from=default_keywords)
    description = seo.MetaTag(max_length=155, populate_from=default_description)

    # Adding some fields for facebook (opengraph)
    og_title = seo.MetaTag(name="og:title",
                           populate_from=default_title,
                           verbose_name="facebook title")

    og_description = seo.MetaTag(name="og:description",
                                 populate_from=default_description,
                                 verbose_name='facebook description')

    og_image = seo.MetaTag(name="og:image",
                           populate_from=default_image, verbose_name='facebook image')

    twitter_card = seo.MetaTag(name="twitter:card", populate_from='summary',
                       verbose_name="twitter card")
    twitter_site = seo.MetaTag(name="twitter:site", populate_from=default_title,
                       verbose_name="twitter site")
    twitter_title = seo.MetaTag(name="twitter:title", populate_from=default_title,
                       verbose_name="twitter title")
    twitter_description = seo.MetaTag(name="twitter:description",
                                 populate_from=default_description,
                                 verbose_name='twitter description')
    twitter_image = seo.MetaTag(name="og:image",
                        populate_from=default_image, verbose_name='twitter image')
                        
    class Meta:
        #use_sites = True
        #use_cache = True
        #use_i18n = True

        #seo_models = ("portfolio",)
        #seo_views = ('news', )
        #backends = ('path', 'modelinstance','model')
        #verbose_name = "My basic example"
        #verbose_name_plural = "My basic examples"
