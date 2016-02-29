GET_METHOD_TEMPLATE="""	/**
	 * Gets %s.
	 *
	 * @return %s
	 */
	%s get%s();"""

SET_METHOD_TEMPLATE="""	/**
	 * Sets %s.
	 *
	 * @param %s
	 *            %s
	 */
	void set%s(%s %s);"""

IS_METHOD_TEMPLATE="""	/**
	 * Checks if this is %s or not.
	 *
	 * @return {@code true} if this is %s
	 */
	%s is%s();"""

INTERFACE_TEMPLATE="""package com.wongnai.domain.model.%s;

/**
 * %s.
 *
 * @author %s
 */
public interface %s extends %s<%s> {
%s
}
"""

IMPLEMENT_TEMPLATE="""package com.wongnai.domain.model.%s.internal;

/**
 * Default implementation of {@link %s}.
 *
 * @author %s
 */
public class %sImpl extends %s<%s> implements %s {
	private static final long serialVersionUID = 1L;
%s
%s
}
"""

GET_METHOD_IMPL_TEMPLATE="""	/**
	 * {@inheritDoc}
	 */
	@Override
	public %s get%s() {
		return %s;
	}"""

SET_METHOD_IMPL_TEMPLATE="""	/**
	 * {@inheritDoc}
	 */
	@Override
	public void set%s(%s %s) {
		this.%s = %s;
	}"""

IS_METHOD_IMPL_TEMPLATE="""	/**
	 * {@inheritDoc}
	 */
	@Override
	public %s get%s() {
		return %s;
	}"""

TEST_TEMPLATE="""package com.wongnai.domain.model.%s.internal;

public class %sImplTest {
	@Before
	public void setUp()() {
            underTest = new %sImpl();
	}
	
%s
}
"""

TEST_METHOD_TEMPLATE="""	@Test
	public void test%s() {
		Assert.assertThat(underTest.get%s(),CoreMatcher.nullValue());
		underTest.set%s(%s);
		Assert.assertThat(underTest.get%s(),CoreMatcher.equalTo(%s));
	}"""

TEST_IS_METHOD_TEMPLATE="""	@Test
	public void test%s() {
		Assert.assertThat(underTest.is%s(),CoreMatcher.equalTo(false));
		underTest.set%s(true);
		Assert.assertThat(underTest.is%s(),CoreMatcher.equalTo(true));
	}"""

FORM_TEMPLATE="""package com.wongnai.web.admin.{packet};
/**
 * The base form of {{@link {interface}}}.
 *
 * @author {auther}
 */
public class CreateOrUpdate{1}Form extends AbstractCreateOrUpdateForm<{interface}, {key}> {{
{variable}

	/**
	 * Fills inputs to the given {name}.
	 *
	 * @param {camel}
	 *            {name}
	 */
	protected void fill({interface} {camel}) {{
		{fill}
	}}
}}
"""
