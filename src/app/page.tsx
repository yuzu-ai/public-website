import ImageFallback from "@/components/ImageFallback";
import { getListPage } from "@/lib/contentParser";
import { markdownify } from "@/lib/utils/textConverter";
import SeoMeta from "@/partials/SeoMeta";
import { Button, Feature } from "@/types";
import { GoogleAnalytics } from "nextjs-google-analytics";

const Home = () => {
  const homepage = getListPage("_index.md");
  const { frontmatter } = homepage;
  const {
    banner,
    features,
  }: {
    banner: { title: string; image: string; content?: string; buttons?: Button[] };
    features: Feature[];
  } = frontmatter;

  return (
    <>
      <GoogleAnalytics trackPageViews gaMeasurementId="G-B3WBLPNZFH" />
      <SeoMeta />
      <section className="section pt-14">
        <div className="container">
          <div className="row justify-center">
            {/* <div className="mb-16 text-center lg:col-7">
              {banner.image && (
                <div className="col-12">
                  <ImageFallback
                    src={banner.image}
                    className="mx-auto"
                    width="600"
                    height="50"
                    alt="banner image"
                    priority
                  />
                </div>
              )}
            </div> */}
            <div className="mb-4 text-center lg:col-7">
              <h1
                className="mb-4"
                dangerouslySetInnerHTML={markdownify(banner.title)}
              />
              <p
                className="mb-8"
                dangerouslySetInnerHTML={markdownify(banner.content ?? "")}
              />
              {banner.buttons && banner.buttons.map((button, index) =>
                button.enable && (
                  <a key={index} className="btn btn-primary mr2" href={button.link} style={{marginRight: '10px'}}>
                    {button.label}
                  </a>
                )
              )}
            </div>
          </div>
        </div>
      </section>

      {/* Rest of the code */}
    </>
  );
};

export default Home;
