from pages.models import ServicePage


def copy_city_structure(
    source_city,
    target_city
):
    """
    Копирует структуру услуг
    из Москвы в новый город.
    """

    parent_map = {}

    parents = ServicePage.objects.filter(
        city=source_city,
        parent__isnull=True
    )

    for page in parents:

        new_page = ServicePage.objects.create(
            city=target_city,
            parent=None,
            title=page.title,
            slug=page.slug,

            title_template_block_1= page.title_template_block_1,
            content_template_block_1=page.content_template_block_1,
            img_template_block_1=page.img_template_block_1,
            img_template_alt_block_1=page.img_template_alt_block_1,
            title_template_block_2= page.title_template_block_2,
            content_template_block_2=page.content_template_block_2,
            img_template_block_2=page.img_template_block_2,
            img_template_alt_block_2=page.img_template_alt_block_2,
            title_template_block_3= page.title_template_block_3,
            content_template_block_3=page.content_template_block_3,
            img_template_block_3=page.img_template_block_3,
            img_template_alt_block_3=page.img_template_alt_block_3,
            title_template_block_4= page.title_template_block_4,
            content_template_block_4=page.content_template_block_4,
            img_template_block_4=page.img_template_block_4,
            img_template_alt_block_4=page.img_template_alt_block_4,


#            content=page.content,
            seo_title=page.seo_title,
            seo_description=page.seo_description,
            seo_keywords=page.seo_keywords,
            is_published=page.is_published,
            show_in_menu=page.show_in_menu,
            no_index=page.no_index,
            sort_order=page.sort_order,
            h1_title=page.h1_title,
            template=page.template,
            )

        parent_map[page.id] = new_page

    # 2 этап
    children = ServicePage.objects.filter(
        city=source_city,
        parent__isnull=False
    )

    for child in children:

        ServicePage.objects.create(
            city=target_city,
            parent=parent_map[child.parent_id],
            title=child.title,
            slug=child.slug,

            title_template_block_1= child.title_template_block_1,
            content_template_block_1=child.content_template_block_1,
            img_template_block_1=child.img_template_block_1,
            img_template_alt_block_1=child.img_template_alt_block_1,
            title_template_block_2= child.title_template_block_2,
            content_template_block_2=child.content_template_block_2,
            img_template_block_2=child.img_template_block_2,
            img_template_alt_block_2=child.img_template_alt_block_2,
            title_template_block_3= child.title_template_block_3,
            content_template_block_3=child.content_template_block_3,
            img_template_block_3=child.img_template_block_3,
            img_template_alt_block_3=child.img_template_alt_block_3,
            title_template_block_4= child.title_template_block_4,
            content_template_block_4=child.content_template_block_4,
            img_template_block_4=child.img_template_block_4,
            img_template_alt_block_4=child.img_template_alt_block_4,


#            content=child.content,
            seo_title=child.seo_title,
            seo_description=child.seo_description,
            seo_keywords=child.seo_keywords,
            is_published=child.is_published,
            show_in_menu=child.show_in_menu,
            no_index=child.no_index,
            sort_order=child.sort_order,
            h1_title=child.h1_title,
            template=child.template,
        )

